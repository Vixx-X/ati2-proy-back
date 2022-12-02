from rest_framework import generics, viewsets
from django.utils.translation import gettext_lazy as _

from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from . import serializers, models


class ContactMeViewSet(viewsets.ModelViewSet):
    queryset = models.ContactMe.objects.all()
    serializer_class = serializers.ContactMeSerializer

class PageSettingView(generics.RetrieveAPIView):
    """
    Page setting data
    """

    permission_classes = (IsAuthenticatedOrReadOnly,)

    @extend_schema(
        summary="Page setting data",
        responses={
            200: OpenApiResponse(
                response=serializers.PageSettingSerializer,
                description="Results",
            ),
        },
    )
    def get(self, *args, **kwargs):
        """
        Return page setting data
        """

        ser = serializers.PageSettingSerializer(
            models.PageSetting.objects.first()
        )

        return Response(ser.data)
