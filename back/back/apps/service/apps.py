from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ServiceConfig(AppConfig):
    name = "back.apps.service"
    label = "service"
    verbose_name = _("service")
