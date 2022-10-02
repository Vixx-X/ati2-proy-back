from django.db import models
from django.utils.translation import gettext_lazy as _

from back.apps.post.models import Post


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
