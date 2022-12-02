from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMe(models.Model):
    email = models.EmailField(
        _("contact email"),
    )

    full_name = models.CharField(
        _("client full name"),
        max_length=255,
    )

    reason = models.CharField(
        _("contact reason"),
        max_length=255,
    )

    body = models.TextField(
        _("contact body"),
    )

    class Meta:
        app_label = "about"
        db_table = "contact_me_submissions"
        verbose_name = _("contact me submission")
        verbose_name_plural = _("contact me submissions")

    def __str__(self):
        return f"About submission #{self.pk}"
