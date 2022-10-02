"""
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Business(models.Model):
    user = models.OneToOneField(
        "user.User",
        on_delete=models.CASCADE,
        related_name="business",
        verbose_name=_("user"),
    )

    name = models.CharField(
        _("name"),
        max_length=255,
    )

    tax_id = models.CharField(
        _("tax id"),
        max_length=255,
    )

    address = models.ForeignKey(
        "address.Address",
        on_delete=models.CASCADE,
        related_name="business",
        verbose_name=_("address"),
    )

    representant = models.OneToOneField(
        "business.Representant",
        on_delete=models.CASCADE,
        related_name="business",
        verbose_name=_("representant"),
    )

    class Meta:
        app_label = "business"
        db_table = "businesses"
        verbose_name = _("business")
        verbose_name_plural = _("businesses")

    def __str__(self):
        return f"Business #{self.id}"


class Representant(models.Model):

    first_name = models.CharField(
        _("first name"),
        max_length=255,
    )

    last_name = models.CharField(
        _("last name"),
        max_length=255,
    )

    email = models.EmailField(
        _("email"),
    )

    phone = PhoneNumberField(
        _("phone"),
    )

    local_phone = PhoneNumberField(
        _("local phone"),
    )

    class Meta:
        app_label = "business"
        db_table = "representants"
        verbose_name = _("representant")
        verbose_name_plural = _("representants")

    def __str__(self):
        return f"Representant #{self.id}"
