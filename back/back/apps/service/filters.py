from django_filters import rest_framework as filters

from .models import ServicePost


class ServicePostFilter(filters.FilterSet):
    class Meta:
        model = ServicePost
        fields = "__all__"
