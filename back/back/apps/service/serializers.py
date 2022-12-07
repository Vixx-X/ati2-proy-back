from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import ServicePost, Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"


class ServicePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePost
        fields = "__all__"
