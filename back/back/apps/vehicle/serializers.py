from typing import List
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from back.apps.address.serializers import AddressSerializer
from back.apps.post.serializers import ContactSerializer
from back.apps.user.models import User

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field

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
    vehicle = VehicleSerializer(
        read_only=True,
    )
    vehicle_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        source="vehicle",
        queryset=Vehicle.objects.all(),
    )

    image_ids = serializers.PrimaryKeyRelatedField(
        source="images",
        queryset=Media.objects.all(),
        many=True,
        allow_empty=True,
    )
    video_ids = serializers.PrimaryKeyRelatedField(
        source="videos",
        queryset=Media.objects.all(),
        many=True,
        allow_empty=True,
    )
    images = serializers.SerializerMethodField()
    videos = serializers.SerializerMethodField()

    def get_images(self, obj) -> List[str]:
        return [image.url for image in obj.images.all()]

    def get_videos(self, obj) -> List[str]:
        return [video.url for video in obj.videos.all()]

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

        videos = validated_data.pop("videos")
        images = validated_data.pop("images")

        obj = VehiclePost.objects.create(**validated_data)

        obj.videos.set(Media.objects.filter(id__in=videos))
        obj.images.set(Media.objects.filter(id__in=images))
        return obj
