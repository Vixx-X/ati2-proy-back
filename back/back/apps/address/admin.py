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
    list_display = ("id", "name", "printable_name", "continent__name")
    list_filter = ("continent__name",)


@admin.register(models.State)
class StateListAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "country__name")
    list_filter = ("country",)


@admin.register(models.City)
class CityListAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_display = ("name", "state__name")
    list_filter = ("state",)


admin.site.register(models.Address)
