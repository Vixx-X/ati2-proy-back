from django_filters import rest_framework as filters

from . import models


class CountryFilter(filters.FilterSet):
    class Meta:
        model = models.Country
        fields = "__all__"


class StateFilter(filters.FilterSet):

    continent = filters.Filter(
        field_name="country__continent",
    )

    class Meta:
        model = models.State
        fields = "__all__"


class CityFilter(filters.FilterSet):

    continent = filters.Filter(
        field_name="state__country__continent",
    )

    country = filters.Filter(
        field_name="state__country",
    )

    class Meta:
        model = models.City
        fields = "__all__"
