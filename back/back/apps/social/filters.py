from django_filters import rest_framework as filters

from . import models


class SocialFilter(filters.FilterSet):

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
    )

    class Meta:
        model = models.Social
        fields = []
