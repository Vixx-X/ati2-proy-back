from typing import Union
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from back.apps.client.serializers import (
    AddressSerializer,
    ClientSerializer,
    SocialSerializer,
)
from back.apps.user.serializers import UserEmployeeSerializer

from back.core.serializers import GenericSerializer
from .models import Business, Employee, Provider, ProviderRepresentant


class BusinessSerializer(GenericSerializer):
    client = ClientSerializer(source="get_client")

    def create(self, validated_data):
        client_data = validated_data.pop("get_client", {})

        business = Business.objects.create(**validated_data)
        client_data["content_object"] = business

        self.client = ClientSerializer()
        self.client.create(validated_data=client_data)

        return business

    class Meta:
        model = Business
        fields = "__all__"


class EmployeeSerializer(GenericSerializer):

    user = UserEmployeeSerializer()
    addresses = AddressSerializer(many=True)
    socials = SocialSerializer(many=True, required=False)
    business_name = serializers.SerializerMethodField()

    def get_business_name(self, obj) -> Union[str, None]:
        return obj.business and obj.business.name or None

    class Meta:
        model = Employee
        fields = [
            "id",
            "phone_number",
            "document_id",
            "contract_modality",
            "business_email",
            "local_phone_number",
            "business",
            "business_name",
            "user",
            "addresses",
            "socials",
        ]

    def create(self, validated_data):
        socials = validated_data.pop("socials")
        addresses = validated_data.pop("addresses")

        user_data = validated_data.pop("user", {})
        self.user = UserEmployeeSerializer()
        user = self.user.create(validated_data=user_data)
        validated_data["user"] = user

        employee = Employee.objects.create(**validated_data)

        for social in socials:
            social["client"] = employee
        self.socials = SocialSerializer(many=True)
        self.socials.create(validated_data=socials)

        for address in addresses:
            address["client"] = employee
        self.addresses = AddressSerializer(many=True)
        self.addresses.create(validated_data=addresses)

        return employee


class ProviderRepresentantSerializer(GenericSerializer):
    addresses = AddressSerializer(many=True)
    socials = SocialSerializer(many=True, required=False)
    user = UserEmployeeSerializer()

    def create(self, validated_data):
        socials = validated_data.pop("socials")
        addresses = validated_data.pop("addresses")

        user_data = validated_data.pop("user", {})
        self.user = UserEmployeeSerializer()
        user = self.user.create(validated_data=user_data)
        validated_data["user"] = user

        client = ProviderRepresentant.objects.create(**validated_data)

        for social in socials:
            social["client"] = client
        self.socials = SocialSerializer(many=True)
        self.socials.create(validated_data=socials)

        for address in addresses:
            address["client"] = client
        self.addresses = AddressSerializer(many=True)
        self.addresses.create(validated_data=addresses)

        return client

    class Meta:
        model = ProviderRepresentant
        fields = [
            "id",
            "addresses",
            "socials",
            "phone_number",
            "local_phone",
            "business_email",
            "user",
        ]


class ProviderSerializer(GenericSerializer):
    representant = ProviderRepresentantSerializer()
    addresses = AddressSerializer(many=True)
    socials = SocialSerializer(many=True, required=False)

    class Meta:
        model = Provider
        fields = [
            "id",
            "representant",
            "addresses",
            "socials",
            "phone_number",
            "name",
            "email",
            "tax_id",
            "website",
            "business",
            "services",
        ]

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)
        self.fields["business"].required = False

    def create(self, validated_data):
        socials = validated_data.pop("socials")
        addresses = validated_data.pop("addresses")
        business = validated_data.pop("business", None)

        representant_data = validated_data.pop("representant", {})
        self.representant = ProviderRepresentantSerializer()
        representant = self.representant.create(validated_data=representant_data)
        validated_data["representant"] = representant

        provider = Provider.objects.create(**validated_data)

        if business:
            businesses = Business.objects.filter(pk__in=business)
            provider.business.set(businesses)

        for social in socials:
            social["client"] = provider
        self.socials = SocialSerializer(many=True)
        self.socials.create(validated_data=socials)

        for address in addresses:
            address["client"] = provider
        self.addresses = AddressSerializer(many=True)
        self.addresses.create(validated_data=addresses)

        return provider

    def update(self, instance, validated_data):
        business = validated_data.pop("business", None)

        if business:
            businesses = Business.objects.filter(pk__in=business)
            instance.business.set(businesses)

        return super().update(instance, validated_data)
