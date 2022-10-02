from rest_framework import generics, viewsets
from django.utils.translation import gettext_lazy as _

from . import serializers, filters, models


class DayOptionListView(generics.ListAPIView):
    queryset = models.DayOption.objects.all()
    serializer_class = serializers.DayOptionSerializer
    filterset_class = filters.DayOptionFilter


class ContactSellerViewSet(viewsets.ModelViewSet):
    queryset = models.ContactSeller.objects.all()
    serializer_class = serializers.ContactSellerSerializer
