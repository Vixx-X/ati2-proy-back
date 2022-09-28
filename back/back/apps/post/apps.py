from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class VehicleConfig(AppConfig):
    name = "back.apps.vehicle"
    label = "vehicle"
    verbose_name = _("vehicle")
