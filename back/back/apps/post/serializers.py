from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import ContactSeller, DayOption, Contact


class ContactSellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSeller
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class DayOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOption
        fields = ["option"]
