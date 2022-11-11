from back.apps.user.serializers import UserRegisterSerializer, UserSerializer
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import NaturalPerson


class NaturalPersonSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = NaturalPerson
        fields = "__all__"

    def create(self, validated_data):
        user = validated_data.pop("user")
        user = UserSerializer().create(user)
        validated_data["user"] = user
        obj = NaturalPerson.objects.create(**validated_data)
        return obj

    # def update(self, instance, validated_data):
    #     user = validated_data.pop("user")
    #     user = UserSerializer().update(instance.user, user)
    #     validated_data["user"] = user
    #     obj = NaturalPerson.objects.update(**validated_data)
    #     return obj


class NaturalPersonRegisterSerializer(NaturalPersonSerializer):
    user = UserRegisterSerializer()

    def create(self, validated_data):
        user = validated_data.pop("user")
        user = UserRegisterSerializer().create(user)
        validated_data["user"] = user
        obj = NaturalPerson.objects.create(**validated_data)
        return obj, obj.user
