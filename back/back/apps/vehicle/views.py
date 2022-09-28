from rest_framework import generics
from django.utils.translation import gettext_lazy as _

from . import serializers, filters, models


class BrandListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.BrandSerializer
    filterset_class = filters.VehicleFilter

class ModelListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.ModelSerializer
    filterset_class = filters.VehicleFilter

class YearListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.YearSerializer
    filterset_class = filters.VehicleFilter

class VehicleListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer
    filterset_class = filters.VehicleFilter

