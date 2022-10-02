from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostConfig(AppConfig):
    name = "back.apps.post"
    label = "post"
    verbose_name = _("post")
