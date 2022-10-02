from rest_framework import generics, viewsets
from django.utils.translation import gettext_lazy as _

from back.apps.user.permissions import IsOwnerOrReadOnly

from . import serializers, filters, models


class ContractModalityListView(generics.ListAPIView):
    queryset = models.ContractModality.objects.all()
    serializer_class = serializers.ContractModalitySerializer


class ProfessionListView(generics.ListAPIView):
    queryset = models.Profession.objects.all()
    serializer_class = serializers.ProfessionSerializer


class JobPostViewSet(viewsets.ModelViewSet):
    user_attr = "author"
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = models.JobPost.objects.all()
    serializer_class = serializers.JobPostSerializer
    filterset_class = filters.JobPostFilter
