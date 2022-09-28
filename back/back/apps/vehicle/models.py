import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


def current_year() -> int:
    """Get the current year"""
    return datetime.date.today().year


def min_valid_year(value):
    """Get the minimun value of a valid year"""
    return MinValueValidator(1950)(value)


def max_valid_year(value):
    """Get the maximum value of a valid year"""
    return MaxValueValidator(current_year())(value)


class Vehicle(models.Model):
    """
    A class that defines the base car details
    """

    brand = models.CharField(
        verbose_name=_("brand"),
        max_length=255,
    )

    model = models.CharField(
        verbose_name=_("model"),
        max_length=255,
    )

    year = models.IntegerField(
        verbose_name=_("year"),
        validators=[min_valid_year, max_valid_year],
    )

    class VehicleType(models.TextChoices):
        HATC = "HB", _("Hatchback")
        SEDA = "SDN", _("Sedan")
        PICK = "PU", _("Pickup truck")
        JEEP = "JEEP", _("Jeep")
        SSUV = "SSUV", _("Small SUV")
        MSUV = "MSUV", _("Mid-size SUV")
        LSUV = "LSUV", _("Full-size SUV")
        STAT = "SW", _("Station wagon")

    type = models.CharField(
        verbose_name=_("type"),
        max_length=4,
        choices=VehicleType.choices,
    )

    date_created = models.DateTimeField(
        _("date created"),
        auto_now_add=True,
        db_index=True,
    )

    date_updated = models.DateTimeField(
        _("date updated"),
        auto_now=True,
        db_index=True,
    )

    class Meta:
        app_label = "vehicle"
        db_table = "vehicles"
        verbose_name = _("vehicle")
        verbose_name_plural = _("vehicles")
        unique_together = ("brand", "model", "year")

    def __str__(self):
        out = [
            self.brand,
            self.model,
            self.year,
        ]
        return " ".join([f"{o}" for o in out if o])
