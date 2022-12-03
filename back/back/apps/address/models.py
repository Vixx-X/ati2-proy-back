"""
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Continent(models.Model):
    name = models.CharField(
        _("Official name"),
        max_length=128,
        unique=True,
    )

    class Meta:
        app_label = "address"
        db_table = "continents"
        verbose_name = _("Continent")
        verbose_name_plural = _("Continents")
        ordering = ("name",)

    def __str__(self):
        return self.name


class Country(models.Model):
    """
    `ISO 3166 Country Codes <https://www.iso.org/iso-3166-country-codes.html>`_

    The field names are a bit awkward, but kept for backwards compatibility.
    pycountry's syntax of alpha2, alpha3, name and official_name seems sane.
    """

    iso_3166_1_a2 = models.CharField(
        _("ISO 3166-1 alpha-2"),
        max_length=2,
        primary_key=True,
    )

    iso_3166_1_a3 = models.CharField(
        _("ISO 3166-1 alpha-3"),
        max_length=3,
        blank=True,
    )

    iso_3166_1_numeric = models.CharField(
        _("ISO 3166-1 numeric"),
        blank=True,
        max_length=3,
    )

    #: The commonly used name; e.g. 'United Kingdom'
    printable_name = models.CharField(
        _("Country name"),
        max_length=128,
        db_index=True,
    )

    #: The full official name of a country
    #: e.g. 'United Kingdom of Great Britain and Northern Ireland'
    name = models.CharField(
        _("Official name"),
        max_length=128,
    )

    phone_code = models.CharField(
        _("Phone code"),
        max_length=5,
        blank=True,
    )

    display_order = models.PositiveSmallIntegerField(
        _("Display order"),
        default=0,
        db_index=True,
        help_text=_("Higher the number, higher the country in the list."),
    )

    continent = models.ForeignKey(
        "address.Continent",
        on_delete=models.CASCADE,
        verbose_name=_("Continent"),
        related_name="countries",
    )

    class Meta:
        app_label = "address"
        db_table = "countries"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        ordering = (
            "-display_order",
            "printable_name",
        )

    def __str__(self):
        return self.printable_name or self.name

    @property
    def code(self):
        """
        Shorthand for the ISO 3166 Alpha-2 code
        """
        return self.iso_3166_1_a2

    @property
    def numeric_code(self):
        """
        Shorthand for the ISO 3166 numeric code.

        :py:attr:`.iso_3166_1_numeric` used to wrongly be a integer field, but has to
        be padded with leading zeroes. It's since been converted to a char
        field, but the database might still contain non-padded strings. That's
        why the padding is kept.
        """
        return "%.03d" % int(self.iso_3166_1_numeric)


class State(models.Model):
    name = models.CharField(
        _("Official name"),
        max_length=128,
        unique=True,
    )

    country = models.ForeignKey(
        "address.Country",
        on_delete=models.CASCADE,
        verbose_name=_("Country"),
        related_name="states",
    )

    class Meta:
        app_label = "address"
        db_table = "states"
        verbose_name = _("State")
        verbose_name_plural = _("States")
        ordering = ("name",)
        unique_together = ("name", "country")

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        _("Official name"),
        max_length=128,
        unique=True,
    )

    state = models.ForeignKey(
        "address.State",
        on_delete=models.CASCADE,
        verbose_name=_("State"),
        related_name="cities",
    )

    class Meta:
        app_label = "address"
        db_table = "cities"
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        ordering = ("name",)
        unique_together = ("name", "state")

    def __str__(self):
        return self.name


class Address(models.Model):

    line1 = models.CharField(
        _("First line of address"),
        max_length=255,
    )

    line2 = models.CharField(
        _("Second line of address"),
        max_length=255,
        blank=True,
    )

    city = models.ForeignKey(
        "address.City",
        on_delete=models.CASCADE,
        verbose_name=_("City"),
    )

    class Meta:
        app_label = "address"
        db_table = "addresses"
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f"address #{self.id}"
