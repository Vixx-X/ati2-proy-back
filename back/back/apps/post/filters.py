from django_filters import rest_framework as filters

from .models import Vehicle

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
