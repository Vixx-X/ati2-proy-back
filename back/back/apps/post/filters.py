from django_filters import rest_framework as filters

from .models import DayOption


class DayOptionFilter(filters.FilterSet):

    option = filters.CharFilter(
        field_name="option",
        lookup_expr="icontains",
    )

    class Meta:
        model = DayOption
        fields = []
