from rest_framework import generics
from django.utils.translation import gettext_lazy as _

from . import serializers, filters, models


class SocialListView(generics.ListAPIView):
    queryset = models.Social.objects.all()
    serializer_class = serializers.SocialSerializer
    filterset_class = filters.SocialFilter
