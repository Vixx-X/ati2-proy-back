import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from back.apps.post.models import Post


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
        CAR = "CAR", _("Car")
        SUV = "SUV", _("SUV")
        TRUCK = "TRUCK", _("Truck")

    type = models.CharField(
        verbose_name=_("type"),
        max_length=4,
        choices=VehicleType.choices,
        null=True,
    )

    date_created = models.DateTimeField(
        _("date created"),
        auto_now_add=True,
        db_index=True,
        null=True,
    )

    date_updated = models.DateTimeField(
        _("date updated"),
        auto_now=True,
        db_index=True,
        null=True,
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


class VehiclePost(Post):

    currency = models.CharField(
        _("currency"),
        max_length=12,
        default="USD",
    )

    sale_price = models.DecimalField(
        _("price"),
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
    )

    rental_price = models.DecimalField(
        _("rental price"),
        decimal_places=2,
        max_digits=12,
        blank=True,
        null=True,
    )

    class SaleType(models.TextChoices):
        RENTAL = "RENT", _("Rental")
        SALE = "SALE", _("Sale")
        BOTH = "BOTH", _("Rental and sale")

    sale_type = models.CharField(
        _("sale type"),
        max_length=4,
        choices=SaleType.choices,
    )

    vehicle = models.ForeignKey(
        "vehicle.Vehicle",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("vehicle"),
    )

    accesories = models.TextField(
        verbose_name=_("accesories"),
    )

    services = models.TextField(
        verbose_name=_("services"),
    )

    class VehicleStateType(models.TextChoices):
        NEW = "NEW", _("new")
        USED = "USED", _("used")

    vehicle_state = models.CharField(
        _("vehicle state"),
        max_length=4,
        choices=VehicleStateType.choices,
    )

    class Meta:
        db_table = "vehicle_posts"
        verbose_name = _("Vehicle post")
        verbose_name_plural = _("Vehicle posts")
