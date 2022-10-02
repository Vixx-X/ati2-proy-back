from django.db import models
from django.utils.translation import gettext_lazy as _

from back.apps.post.models import Post


class ContractModality(models.Model):
    name = models.CharField(
        _("contact modality name"),
        max_length=128,
        unique=True,
        primary_key=True,
    )

    class Meta:
        app_label = "job"
        db_table = "contact_modalities"
        verbose_name = _("Contract Modality")
        verbose_name_plural = _("Contract Modalities")
        ordering = ("name",)

    def __str__(self):
        return self.name


class Profession(models.Model):
    name = models.CharField(
        _("Profession name"),
        max_length=128,
        unique=True,
        primary_key=True,
    )

    class Meta:
        app_label = "job"
        db_table = "professions"
        verbose_name = _("Profession")
        verbose_name_plural = _("Professions")
        ordering = ("name",)

    def __str__(self):
        return self.name


class JobPost(Post):

    title = models.CharField(
        _("title"),
        max_length=128,
    )

    schedule = models.CharField(
        _("schedule"),
        max_length=180,
    )

    modality = models.ForeignKey(
        "job.ContractModality",
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name=_("contact modality"),
    )

    supervisors = models.ManyToManyField(
        "job.Profession",
        related_name="+",
    )

    interactors = models.ManyToManyField(
        "job.Profession",
        related_name="+",
    )

    class Meta:
        db_table = "job_posts"
        verbose_name = _("Job post")
        verbose_name_plural = _("Job posts")
