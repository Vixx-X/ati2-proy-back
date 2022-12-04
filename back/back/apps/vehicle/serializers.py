from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from back.apps.address.serializers import AddressSerializer
from back.apps.post.serializers import ContactSerializer
from back.apps.user.models import User

from .models import Vehicle, VehiclePost
from back.apps.media.models import Media


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


class VehiclePostSerializer(serializers.ModelSerializer):
    contact = ContactSerializer()
    address = AddressSerializer()
    author = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )
    media = serializers.PrimaryKeyRelatedField(
        queryset=Media.objects.all(),
        many=True,
        allow_empty=True,
    )

    class Meta:
        model = VehiclePost
        fields = "__all__"

    def create(self, validated_data):
        contact = validated_data.pop("contact")
        address = validated_data.pop("address")

        contact = ContactSerializer().create(contact)
        validated_data["contact"] = contact

        address = AddressSerializer().create(address)
        validated_data["address"] = address

        obj = VehiclePost.objects.create(**validated_data)
        return obj
