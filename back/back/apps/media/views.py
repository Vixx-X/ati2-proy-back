from rest_framework import viewsets
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import serializers, models, permissions


class MediaViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        permissions.OwnMediaPermission,
    ]
    queryset = models.Media.objects.all()
    serializer_class = serializers.MediaSerializer
