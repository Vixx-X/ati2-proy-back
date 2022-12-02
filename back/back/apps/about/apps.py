from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AboutConfig(AppConfig):
    name = "back.apps.about"
    label = "about"
    verbose_name = _("about")
