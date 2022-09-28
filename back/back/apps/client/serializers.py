from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.reverse import reverse
from back.apps.user.serializers import UserEmployeeSerializer

from back.core.serializers import GenericSerializer
from .models import Client, ParticularClient, Social, Address, Country


class CountrySerializer(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_img(self, obj):
        code = obj.iso_3166_1_a2
        return f"https://flagcdn.com/w20/{code}.png"

    class Meta:
        model = Country
        fields = "__all__"


class AddressSerializer(GenericSerializer):
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
    )

    class Meta:
        model = Address
        fields = [
            "line1",
            "line2",
            "city",
            "state",
            "country",
        ]


class SocialSerializer(GenericSerializer):
    class Meta:
        model = Social
        fields = [
            "name",
            "value",
        ]


class ClientSerializer(GenericSerializer):
    addresses = AddressSerializer(many=True)
    socials = SocialSerializer(many=True, required=False)
    url = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.URI)
    def get_url(self, obj):
        if obj.type == "business":
            return reverse(
                "business:business-detail",
                args=[obj.pk],
                request=self.context["request"],
            )
        return reverse(
            "client:particularclient-detail",
            args=[obj.pk],
            request=self.context["request"],
        )

    class Meta:
        model = Client
        fields = [
            "url",
            "type",
            "phone_number",
            "whatsapp",
            "fav_course",
            "notification_frecuency",
            "offered_services",
            "addresses",
            "socials",
        ]

    def create(self, validated_data):
        validated_data.pop("id", None)
        socials = validated_data.pop("socials")
        addresses = validated_data.pop("addresses")

        client = Client.objects.create(**validated_data)

        for social in socials:
            social["client"] = client
        self.socials = SocialSerializer(many=True)
        self.socials.create(validated_data=socials)

        for address in addresses:
            address["client"] = client
        self.addresses = AddressSerializer(many=True)
        self.addresses.create(validated_data=addresses)

        return client


class ParticularClientSerializer(GenericSerializer):
    client = ClientSerializer(source="get_client")
    user = UserEmployeeSerializer()

    class Meta:
        model = ParticularClient
        fields = [
            "id",
            "user",
            "type",
            "company",
            "client",
        ]

    def create(self, validated_data):
        validated_data.pop("id", None)
        client_data = validated_data.pop("get_client", {})

        user_data = validated_data.pop("user", {})
        self.user = UserEmployeeSerializer()
        user = self.user.create(validated_data=user_data)
        validated_data["user"] = user

        particular_client = ParticularClient.objects.create(**validated_data)
        client_data["content_object"] = particular_client

        self.client = ClientSerializer()
        self.client.create(validated_data=client_data)

        return particular_client
