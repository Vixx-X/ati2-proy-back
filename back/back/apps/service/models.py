from django.db import models
from django.utils.translation import gettext_lazy as _

from back.apps.post.models import Post


class Service(models.Model):
    name = models.CharField(
        _("name"),
        max_length=255,
        unique=True,
        primary_key=True,
    )

    class Meta:
        db_table = "services"
        verbose_name = _("service")
        verbose_name_plural = _("services")
        ordering = ("name",)

    def __str__(self):
        return self.name


class ServicePost(Post):

    title = models.CharField(
        _("title"),
        max_length=128,
    )

    url = models.URLField(
        _("url"),
    )

    class Meta:
        db_table = "service_posts"
        verbose_name = _("Service post")
        verbose_name_plural = _("Service posts")
