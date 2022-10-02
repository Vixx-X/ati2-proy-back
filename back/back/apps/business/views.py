from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from back.apps.user.permissions import IsOwnerOrReadOnly
from back.apps.user.views import RegistrationMixin

from .serializers import BusinessSerializer, BussinessRegisterSerializer
from .models import Business


class BusinessViewSet(viewsets.ModelViewSet):
    """
    Entrypoint for businesses
    """

    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class BusinessRegistrationView(generics.CreateAPIView, RegistrationMixin):
    register_serializer_class = BussinessRegisterSerializer
    serializer_class = BusinessSerializer
    permission_classes = (AllowAny,)
