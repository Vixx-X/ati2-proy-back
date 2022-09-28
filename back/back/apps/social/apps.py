from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SocialConfig(AppConfig):
    name = "back.apps.social"
    label = "social"
    verbose_name = _("social")
