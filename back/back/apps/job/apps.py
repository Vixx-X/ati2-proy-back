from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class JobConfig(AppConfig):
    name = "back.apps.job"
    label = "job"
    verbose_name = _("job")
