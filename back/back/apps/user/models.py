from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from django_otp.plugins.otp_email.models import EmailDevice as BaseEmailDevice

from back.apps.user.mails import SendOTPMail


class UserSocial(models.Model):
    value = models.CharField(
        _("value"),
        max_length=255,
        blank=True,
        null=True,
    )

    social = models.ForeignKey(
        "social.Social",
        on_delete=models.CASCADE,
        verbose_name=_("social"),
        related_name="user_socials",
        null=True,
    )

    notification_method = models.ForeignKey(
        "user.NotificationMethod",
        on_delete=models.CASCADE,
        verbose_name=_("notification method"),
        related_name="socials",
    )

    class Meta:
        app_label = "user"
        db_table = "user_socials"
        verbose_name = _("user social")
        verbose_name_plural = _("user socials")

    def __str__(self):
        return f"{self.social} : {self.value}"


class NotificationMethod(models.Model):
    email = models.EmailField(
        _("send notification"),
        blank=True,
        null=True,
    )

    sms = PhoneNumberField(
        _("text message"),
        blank=True,
        null=True,
    )

    other = models.TextField(
        _("other method"),
        blank=True,
        null=True,
    )

    facebook = models.EmailField(
        _("facebook mail"),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = "user"
        db_table = "notification_methods"
        verbose_name = _("notification method")
        verbose_name_plural = _("notification methods")

    def __str__(self):
        return f"{self.id}"


class NotificationSetting(models.Model):
    active = models.BooleanField(
        _("send notification"),
    )

    frecuency = models.CharField(
        _("frecuency"),
        max_length=255,
    )

    notification_method = models.OneToOneField(
        "user.NotificationMethod",
        on_delete=models.CASCADE,
        verbose_name=_("notification methods"),
        related_name="notification_setting",
    )

    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="notification_setting",
    )

    class Meta:
        app_label = "user"
        db_table = "notification_settings"
        verbose_name = _("notification setting")
        verbose_name_plural = _("notification settings")

    def __str__(self):
        return f"{self.id}"


class PaymentInfo(models.Model):

    source_bank = models.CharField(
        _("source bank"),
        max_length=512,
    )

    target_bank = models.CharField(
        _("target bank"),
        max_length=512,
    )

    country = models.ForeignKey(
        "address.Country",
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
        related_name="bank",
    )

    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="payment_info",
    )

    class Meta:
        app_label = "user"
        db_table = "payment_info"
        verbose_name = _("payment info")
        verbose_name_plural = _("payment infos")

    def __str__(self):
        return f"{self.id}"


class AboutWebSite(models.Model):

    web = models.BooleanField(
        _("web"),
    )

    socials = models.ManyToManyField(
        "social.Social",
        verbose_name=_("social"),
        related_name="+",
    )

    friends = models.BooleanField(
        _("friends"),
    )

    other = models.TextField(
        _("other method"),
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="about_website",
    )

    class Meta:
        app_label = "user"
        db_table = "about_website"
        verbose_name = _("about website")
        verbose_name_plural = _("abouts website")

    def __str__(self):
        return f"{self.id}"


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    class Languages(models.TextChoices):
        ES = "ES", _("Español")
        EN = "EN", _("English")

    language = models.CharField(
        verbose_name=_("language"),
        default=Languages.ES,
        max_length=4,
        choices=Languages.choices,
    )

    first_name = None
    last_name = None

    @classmethod
    def get_identifier_fields(cls):
        return ["email", "natural_person__document_id", "business__tax_id"]


class EmailDevice(BaseEmailDevice):
    """
    A :class:`~django_otp.models.SideChannelDevice` that delivers a token to
    the email address saved in this object or alternatively to the user's
    registered email address (``user.email``).
    The tokens are valid for :setting:`OTP_EMAIL_TOKEN_VALIDITY` seconds. Once
    a token has been accepted, it is no longer valid.
    Note that if you allow users to reset their passwords by email, this may
    provide little additional account security. It may still be useful for,
    e.g., requiring the user to re-verify their email address on new devices.
    .. attribute:: email
        *EmailField*: An alternative email address to send the tokens to.
    """

    class Meta:
        proxy = True

    def generate_challenge(self, extra_context=None):
        """
        Generates a random token and emails it to the user.

        :param extra_context: Additional context variables for rendering the
            email template.
        :type extra_context: dict

        """
        self.generate_token(valid_secs=settings.OTP_EMAIL_TOKEN_VALIDITY)

        context = {"token": self.token, **(extra_context or {})}

        mail = SendOTPMail()
        mail.set_context(**context)
        mail.send([self.user.email])

        message = _("sent by email")

        return message
