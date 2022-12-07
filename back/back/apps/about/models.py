from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class InvalidSave(Exception):
    """
    Raised when someone is trying to save another Setting, while
    there is already one in existance.
    """


class ContactMe(models.Model):
    email = models.EmailField(
        _("contact email"),
    )

    full_name = models.CharField(
        _("client full name"),
        max_length=255,
    )

    reason = models.CharField(
        _("contact reason"),
        max_length=255,
    )

    class Meta:
        app_label = "about"
        db_table = "contact_me_submissions"
        verbose_name = _("contact me submission")
        verbose_name_plural = _("contact me submissions")

    def __str__(self):
        return f"About submission #{self.pk}"


class SingletonModel(models.Model):
    singleton_instance_id = 1

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = self.singleton_instance_id
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def get_singleton(cls):
        obj, created = cls.objects.get_or_create(pk=cls.singleton_instance_id)
        return obj


class PageSetting(SingletonModel):
    email = models.EmailField(
        _("page email"),
        blank=True,
    )

    image_limit = models.IntegerField(
        _("image limit"),
        default=10,
    )

    video_limit = models.IntegerField(
        _("video limit"),
        default=5,
    )

    phone = PhoneNumberField(
        _("phone number"),
        blank=True,
    )

    local_phone = PhoneNumberField(
        _("local phone number"),
        blank=True,
    )

    first_name = models.CharField(
        _("owner first name"),
        max_length=128,
    )

    last_name = models.CharField(
        _("owner last name"),
        max_length=128,
    )

    bank_detail = models.JSONField(
        _("bank detail"),
    )

    class Meta:
        app_label = "about"
        db_table = "page_setting"
        verbose_name = _("page setting")
        verbose_name_plural = _("page settings")

    def __str__(self):
        return f"Page setting"
