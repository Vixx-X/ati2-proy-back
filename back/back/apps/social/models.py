"""
"""
from django.db import models
from django.utils.translation import gettext_lazy as _


class Social(models.Model):
    name = models.CharField(
        _("Social name"),
        max_length=128,
        unique=True,
        primary_key=True,
    )

    class Meta:
        app_label = "social"
        db_table = "socials"
        verbose_name = _("Social")
        verbose_name_plural = _("Socials")
        ordering = ("name",)

    def __str__(self):
        return self.name
