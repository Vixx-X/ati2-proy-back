from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from . import models


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        fields = "__all__"
