from rest_framework import viewsets
from django.utils.translation import gettext_lazy as _

from . import serializers, models


class ContactMeViewSet(viewsets.ModelViewSet):
    queryset = models.ContactMe.objects.all()
    serializer_class = serializers.ContactMeSerializer
