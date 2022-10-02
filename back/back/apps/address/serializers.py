from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from . import models


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Continent
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"
