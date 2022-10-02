from rest_framework.views import APIView
from drf_spectacular.extensions import (
    OpenApiSerializerExtension,
    OpenApiSerializerFieldExtension,
    OpenApiViewExtension,
)


class Fix1(OpenApiViewExtension):
    target_class = "back.apps.business.views.BusinessRegistrationView"

    def view_replacement(self):
        from back.apps.business.serializers import BussinessRegisterSerializer

        class Fixed(self.target_class):
            serializer_class = BussinessRegisterSerializer

        return Fixed


class Fix2(OpenApiViewExtension):
    target_class = "back.apps.client.views.NaturalPersonRegistrationView"

    def view_replacement(self):
        from back.apps.client.serializers import NaturalPersonRegisterSerializer

        class Fixed(self.target_class):
            serializer_class = NaturalPersonRegisterSerializer

        return Fixed
