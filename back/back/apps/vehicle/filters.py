from django_filters import rest_framework as filters

from .models import Vehicle, VehiclePost


class VehicleFilter(filters.FilterSet):

    brand = filters.CharFilter(
        field_name="brand",
        lookup_expr="icontains",
    )

    model = filters.CharFilter(
        field_name="model",
        lookup_expr="icontains",
    )

    year = filters.CharFilter(
        field_name="year",
        lookup_expr="icontains",
    )

    class Meta:
        model = Vehicle
        fields = []


class VehiclePostFilter(filters.FilterSet):
    brand = filters.CharFilter(
        field_name="vehicle__brand",
        lookup_expr="icontains",
    )

    model = filters.CharFilter(
        field_name="vehicle__model",
        lookup_expr="icontains",
    )

    year = filters.CharFilter(
        field_name="vehicle__year",
        lookup_expr="icontains",
    )

    continent = filters.Filter(
        field_name="address__continent",
    )

    country = filters.Filter(
        field_name="address__country",
    )

    state = filters.Filter(
        field_name="address__state",
    )

    class Meta:
        model = VehiclePost
        fields = "__all__"
