from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Media
        fields = "__all__"
