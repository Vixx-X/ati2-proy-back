from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddressConfig(AppConfig):
    name = "back.apps.address"
    label = "address"
    verbose_name = _("address")
