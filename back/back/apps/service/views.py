from rest_framework import viewsets
from django.utils.translation import gettext_lazy as _

from back.apps.user.permissions import IsOwnerOrReadOnly

from . import serializers, filters, models


class ServicePostViewSet(viewsets.ModelViewSet):
    user_attr = "author"
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = models.ServicePost.objects.all()
    serializer_class = serializers.ServicePostSerializer
    filterset_class = filters.ServicePostFilter
