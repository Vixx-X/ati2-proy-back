from rest_framework import generics
from django.utils.translation import gettext_lazy as _

from . import serializers, filters, models


class ContinentListView(generics.ListAPIView):
    queryset = models.Continent.objects.all()
    serializer_class = serializers.ContinentSerializer


class CountryListView(generics.ListAPIView):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    filterset_class = filters.CountryFilter


class StateListView(generics.ListAPIView):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    filterset_class = filters.StateFilter


class CityListView(generics.ListAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    filterset_class = filters.CityFilter
