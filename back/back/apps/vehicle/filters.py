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
        fields = [
            "type",
        ]


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
        field_name="address__city__state__country__continent",
    )

    country = filters.Filter(
        field_name="address__city__state__country",
    )

    state = filters.Filter(
        field_name="address__city__state",
    )

    sale_price = filters.RangeFilter()
    rental_price = filters.RangeFilter()

    class Meta:
        model = VehiclePost
        fields = "__all__"
