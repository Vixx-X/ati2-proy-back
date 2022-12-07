from django_filters import rest_framework as filters

from .models import ServicePost, Service


class ServiceFilter(filters.FilterSet):
    class Meta:
        model = Service
        fields = "__all__"


class ServicePostFilter(filters.FilterSet):
    class Meta:
        model = ServicePost
        fields = "__all__"
