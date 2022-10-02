from rest_framework import generics, viewsets

from back.apps.user.permissions import IsOwnerOrReadOnly
from back.apps.user.views import RegistrationMixin

from .serializers import NaturalPersonRegisterSerializer, NaturalPersonSerializer

from .models import NaturalPerson


class NaturalPersonViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for natural person
    """

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = NaturalPerson.objects.all()
    serializer_class = NaturalPersonSerializer


class NaturalPersonRegistrationView(RegistrationMixin, generics.CreateAPIView):
    register_serializer_class = NaturalPersonRegisterSerializer
    serializer_class = NaturalPersonSerializer
