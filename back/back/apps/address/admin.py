from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


@admin.register(models.Continent)
class ContinentListAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("id", "name")


@admin.register(models.Country)
class CountryListAdmin(admin.ModelAdmin):
    search_fields = ("iso_3166_1_a2", "name", "printable_name")
    list_display = ("name", "printable_name", "continent")
    list_filter = ("continent",)


@admin.register(models.State)
class StateListAdmin(admin.ModelAdmin):
    search_fields = ("name", "country__name")
    list_display = ("id", "name", "country")
    list_filter = ("country",)


@admin.register(models.City)
class CityListAdmin(admin.ModelAdmin):
    search_fields = ("name", "state__name", "state__country__name")
    list_display = ("id", "name", "state")
    list_filter = ("state",)


admin.site.register(models.Address)
