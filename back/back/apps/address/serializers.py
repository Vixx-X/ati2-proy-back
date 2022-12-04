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
    continent = ContinentSerializer(
        read_only=True,
    )
    continent_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="continent",
        queryset=models.Continent.objects.all(),
    )

    img = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_img(self, obj):
        code = obj.iso_3166_1_a2.lower()
        return f"https://flagcdn.com/w20/{code}.png"

    class Meta:
        model = models.Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer(
        read_only=True,
    )
    country_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="country",
        queryset=models.Country.objects.all(),
    )

    class Meta:
        model = models.State
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    state = StateSerializer(
        read_only=True,
    )
    state_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="state",
        queryset=models.State.objects.all(),
    )

    class Meta:
        model = models.City
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer(
        read_only=True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="city",
        queryset=models.City.objects.all(),
    )

    class Meta:
        model = models.Address
        fields = "__all__"
