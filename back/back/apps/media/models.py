from django.db import models
from django.utils.translation import gettext_lazy as _


class Media(models.Model):
    """
    A class that defines the media details
    """

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="media",
        verbose_name=_("user"),
    )

    file = models.FileField(
        verbose_name=_("file"),
        upload_to="uploads/%Y/%m/%d/",
    )

    date_created = models.DateTimeField(
        _("date created"),
        auto_now_add=True,
        db_index=True,
    )

    date_updated = models.DateTimeField(
        _("date updated"),
        auto_now=True,
        db_index=True,
    )

    class Meta:
        app_label = "media"
        db_table = "medias"
        verbose_name = _("media")
        verbose_name_plural = _("multimedias")

    def __str__(self):
        return "media {self.pk}"
