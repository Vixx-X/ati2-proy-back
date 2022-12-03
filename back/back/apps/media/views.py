from rest_framework import viewsets
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser

from . import serializers, models, permissions


class MediaViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        permissions.OwnMediaPermission,
    ]
    parser_classes = (
        MultiPartParser,
        FormParser,
        JSONParser,
    )
    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer
