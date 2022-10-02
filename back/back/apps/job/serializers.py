from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import ContractModality, Profession, JobPost


class ContractModalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractModality
        fields = ["name"]


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = ["name"]


class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = "__all__"
