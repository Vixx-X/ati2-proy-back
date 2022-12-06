from typing import List
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from back.apps.address.serializers import AddressSerializer
from back.apps.post.serializers import ContactSerializer
from back.apps.user.models import User

from rest_framework.utils import model_meta

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
        return [
            self.context["request"].build_absolute_uri(image.file.url)
            for image in obj.images.all()
        ]

    def get_videos(self, obj) -> List[str]:
        return [
            self.context["request"].build_absolute_uri(video.file.url)
            for video in obj.videos.all()
        ]

    class Meta:
        model = VehiclePost
        fields = "__all__"

    def update(self, instance, validated_data):
        contact = validated_data.pop("contact")
        address = validated_data.pop("address")

        contact = ContactSerializer().update(instance.contact, contact)
        instance.contact = contact

        address = AddressSerializer().update(instance.address, address)
        instance.address = address

        videos = validated_data.pop("videos")
        images = validated_data.pop("images")

        info = model_meta.get_field_info(instance)

        # Simply set each attribute on the instance, and then save it.
        # Note that unlike `.create()` we don't need to treat many-to-many
        # relationships as being a special case. During updates we already
        # have an instance pk for the relationships to be associated with.
        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        instance.save()

        # Note that many-to-many fields are set after updating instance.
        # Setting m2m fields triggers signals which could potentially change
        # updated instance and we do not want it to collide with .update()
        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        instance.videos.set(videos)
        instance.images.set(images)

        return instance

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

        obj.videos.set(videos)
        obj.images.set(images)

        return obj
