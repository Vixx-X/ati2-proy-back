from django.db.models import Q
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.urls.base import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.forms import _unicode_ci_compare
from django.contrib.sites.shortcuts import get_current_site
from django_otp import verify_token
from back.apps.user import mails
from back.apps.social.models import Social

from . import models

User = models.User


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "is_superuser", "groups", "user_permissions"]


class UserSocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserSocial
        exclude = ["notification_method"]


class NotificationMethodSerializer(serializers.ModelSerializer):
    socials = UserSocialSerializer(many=True)

    class Meta:
        model = models.NotificationMethod
        fields = "__all__"

    def validate(self, attrs):
        if not attrs:
            raise serializers.ValidationError(
                _("Must include at least one notification method")
            )
        return super().validate(attrs)

    def create(self, validated_data):
        socials = validated_data.pop("socials")
        obj = models.NotificationMethod.objects.create(**validated_data)
        for social in socials:
            social["notification_method"] = obj
            UserSocialSerializer().create(validated_data=social)
        return obj


class NotificationSettingSerializer(serializers.ModelSerializer):
    notification_method = NotificationMethodSerializer()

    class Meta:
        model = models.NotificationSetting
        exclude = ["user"]

    def create(self, validated_data):
        notification_method = validated_data.pop("notification_method")
        obj = NotificationMethodSerializer().create(validated_data=notification_method)
        validated_data["notification_method"] = obj
        obj = models.NotificationSetting.objects.create(**validated_data)
        return obj


class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentInfo
        exclude = ["user"]


class AboutWebSiteSerializer(serializers.ModelSerializer):
    socials = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Social.objects.all(),
    )

    class Meta:
        model = models.AboutWebSite
        exclude = ["user"]


class UserSerializer(serializers.ModelSerializer):
    notification_setting = NotificationSettingSerializer()
    payment_info = PaymentInfoSerializer()
    about_website = AboutWebSiteSerializer()

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        notification_setting = validated_data.pop("notification_setting")
        payment_info = validated_data.pop("payment_info")
        about_website = validated_data.pop("about_website")
        obj = models.User.objects.create_user(**validated_data, is_active=True)
        notification_setting["user"] = obj
        payment_info["user"] = obj
        about_website["user"] = obj
        NotificationSettingSerializer().create(notification_setting)
        PaymentInfoSerializer().create(payment_info)
        AboutWebSiteSerializer().create(about_website)
        return obj


def get_password_reset_url(user, token_generator=default_token_generator):
    """
    Generate a password-reset URL for a given user
    """
    kwargs = {
        "token": token_generator.make_token(user),
        "uidb64": urlsafe_base64_encode(force_bytes(user.id)),
    }
    return reverse("password-reset-confirm", kwargs=kwargs)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    document_id = serializers.CharField(required=False)

    def validate(self, attrs):
        if not attrs.get("email") and not attrs.get("document_id"):
            raise serializers.ValidationError(
                _("This field is required"),
                code="no_identifier_field",
            )
        return super().validate(attrs)

    def get_users(self, email_or_document_id):
        """Given an email, return matching user(s) who should receive a reset.
        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        identifier_fields = User.get_identifier_fields()
        query = Q()
        for field_name in identifier_fields:
            query |= Q(**{"%s__iexact" % field_name: email_or_document_id})
        query &= Q(is_active=True)
        active_users = User._default_manager.filter(query)
        return (
            u
            for u in active_users
            if u.has_usable_password()
            and any(
                _unicode_ci_compare(email_or_document_id, getattr(u, field_name))
                for field_name in identifier_fields
            )
        )

    def save(self, domain_override=None, request=None):
        """
        Generates a one-use only link for resetting password and sends to the
        user.
        """
        site = get_current_site(request)
        if domain_override is not None:
            site.domain = site.name = domain_override
        for user in self.get_users(self.data.get("email") or self.data.get("document_id")):
            self.send_password_reset_email(site, user)
            return user
        raise serializers.ValidationError(
            _("There is no active user with these credentials"),
            code="no_user",
        )

    def send_password_reset_email(self, site, user):
        extra_context = {
            "user": user,
            "url": str(site) + get_password_reset_url(user),
        }
        mail = mails.ResetPasswordMail()
        mail.set_context(**extra_context)
        mail.send([user.email])


class PasswordSerializer(serializers.Serializer):
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()

    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.user = self.context["view"].object

    def validate(self, attrs):
        password1 = attrs["new_password1"]
        password2 = attrs["new_password2"]
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    _("The two password fields didn’t match."),
                    code="password_mismatch",
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self):
        password = self.validated_data
        self.user.set_password(password)
        self.user.save()
        return self.user


class OTPRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    device = serializers.CharField(read_only=True)


class OTPChallengeSerializer(serializers.Serializer):
    device = serializers.CharField()
    token = serializers.CharField()

    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.user = self.context["request"].user

    def validate(self, attrs):
        ret = super().validate(attrs)
        device = attrs["device"]
        token = attrs["token"]
        verified = (
            verify_token(user=self.user, device_id=device, token=token) is not None
        )
        if not verified:
            raise ValidationError(
                _("The token submitted is invalid."),
                code="token_invalid",
            )
        return ret


class ChangePasswordSerializer(OTPChallengeSerializer):
    old_password = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )
    new_password1 = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )
    new_password2 = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )

    def validate_old_password(self, old_password):
        if not self.user.check_password(old_password):
            raise ValidationError(
                _("The old password didn’t match."),
                code="wrong_password",
            )
        return old_password

    def validate(self, attrs):
        super().validate(attrs)

        password1 = attrs["new_password1"]
        password2 = attrs["new_password2"]
        if password1 != password2:
            raise ValidationError(
                _("The two password fields didn’t match."),
                code="password_mismatch",
            )

        password_validation.validate_password(password2, self.user)
        return password2

    def save(self):
        password = self.validated_data
        self.user.set_password(password)
        self.user.save()
        return self.user


class ChangeEmailSerializer(OTPChallengeSerializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        if email == self.user.email:
            raise ValidationError(
                _("The email has not changed."),
                code="repeated_email",
            )

    def validate(self, attrs):
        super().validate(attrs)
        return attrs["email"]

    def save(self):
        email = self.validated_data
        self.user.email = email
        self.user.save()
        return self.user


class UserRegisterSerializer(UserSerializer):
    password1 = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )
    password2 = serializers.CharField(
        required=True,
        style={"input_type": "password"},
    )

    def validate(self, attrs):
        if attrs["password1"] != attrs["password2"]:
            raise serializers.ValidationError(
                "Passwords do not match",
                code="password_mismatch",
            )

        password_validation.validate_password(attrs["password1"])
        return attrs

    def create(self, validated_data):
        validated_data["password"] = validated_data.pop("password1")
        validated_data.pop("password2")
        return super().create(validated_data)

    class Meta(UserSerializer.Meta):
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "language",
            "about_website",
            "payment_info",
            "notification_setting",
        ]
