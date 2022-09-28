from django_filters import rest_framework as filters

from . import models


class CountryFilter(filters.FilterSet):
    class Meta:
        model = models.Country
        fields = ["continent"]


class StateFilter(filters.FilterSet):
    class Meta:
        model = models.State
        fields = ["country"]


class CityFilter(filters.FilterSet):
    class Meta:
        model = models.City
        fields = ["state"]
