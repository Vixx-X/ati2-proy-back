from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import ContactMe


class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMe
        fields = "__all__"
