from rest_framework import generics, viewsets
from django.utils.translation import gettext_lazy as _

from back.apps.user.permissions import IsOwnerOrReadOnly

from . import serializers, filters, models


class BrandListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all().distinct("brand")
    serializer_class = serializers.BrandSerializer
    filterset_class = filters.VehicleFilter


class ModelListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all().distinct("model")
    serializer_class = serializers.ModelSerializer
    filterset_class = filters.VehicleFilter


class YearListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all().distinct("year")
    serializer_class = serializers.YearSerializer
    filterset_class = filters.VehicleFilter


class VehicleListView(generics.ListAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer
    filterset_class = filters.VehicleFilter

class VehicleDetailView(generics.RetrieveAPIView):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer


class VehiclePostViewSet(viewsets.ModelViewSet):
    user_attr = "author"
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = models.VehiclePost.objects.all()
    serializer_class = serializers.VehiclePostSerializer
    filterset_class = filters.VehiclePostFilter
