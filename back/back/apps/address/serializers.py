from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

from . import models


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Continent
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_img(self, obj):
        code = obj.iso_3166_1_a2
        return f"https://flagcdn.com/w20/{code}.png"

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
