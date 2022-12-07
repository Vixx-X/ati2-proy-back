"""
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class NaturalPerson(models.Model):
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="natural_person",
        verbose_name=_("user"),
    )

    first_name = models.CharField(
        _("first name"),
        max_length=150,
        blank=True,
    )

    last_name = models.CharField(
        _("last name"),
        max_length=150,
        blank=True,
    )

    email = models.EmailField(
        _("email address"),
        blank=True,
    )

    document_id = models.CharField(
        _("document id"),
        max_length=150,
        unique=True,
    )

    phone = PhoneNumberField(
        _("phone number"),
        blank=True,
    )

    local_phone = PhoneNumberField(
        _("local phone number"),
        blank=True,
    )

    country = models.ForeignKey(
        "address.Country",
        verbose_name=_("country"),
        on_delete=models.CASCADE,
    )

    class Meta:
        app_label = "client"
        db_table = "natural_person"
        verbose_name = _("natural person")
        verbose_name_plural = _("natural persons")

    def __str__(self):
        return f"Natural person #{self.id}"
