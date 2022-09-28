from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Vehicle


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ["brand"]

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ["model"]

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ["year"]

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"

