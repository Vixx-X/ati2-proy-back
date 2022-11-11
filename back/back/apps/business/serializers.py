from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from back.apps.address.serializers import AddressSerializer

from back.apps.user.serializers import UserRegisterSerializer, UserSerializer


from . import models


class RepresentantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Representant
        fields = "__all__"


class BusinessSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    representant = RepresentantSerializer()
    address = AddressSerializer()

    class Meta:
        model = models.Business
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop("user")
        representant = validated_data.pop("representant")
        address = validated_data.pop("address")

        user = UserSerializer().create(user)
        validated_data["user"] = user

        representant = RepresentantSerializer().create(representant)
        validated_data["representant"] = representant

        address = AddressSerializer().create(address)
        validated_data["address"] = address

        obj = models.Business.objects.create(**validated_data)
        return obj


class BussinessRegisterSerializer(BusinessSerializer):
    user = UserRegisterSerializer()

    def create(self, validated_data):
        user = validated_data.pop("user")
        representant = validated_data.pop("representant")
        address = validated_data.pop("address")

        user = UserRegisterSerializer().create(user)
        validated_data["user"] = user

        representant = RepresentantSerializer().create(representant)
        validated_data["representant"] = representant

        address = AddressSerializer().create(address)
        validated_data["address"] = address

        obj = models.Business.objects.create(**validated_data)
        return obj, obj.user
