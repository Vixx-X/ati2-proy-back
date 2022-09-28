"""
"""
from typing import Literal, Union
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class CommonClient(models.Model):

    phone_number = PhoneNumberField(
        _("phone number"),
        blank=True,
    )

    fav_course = models.CharField(
        _("favorite course"),
        max_length=255,
    )

    notification_frecuency = models.CharField(
        _("notification frecuency"),
        max_length=255,
    )

    class Meta:
        app_label = "client"
        db_table = "common_client_data"
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return f"Client #{self.id}"


class Client(CommonClient):

    offered_services = models.CharField(
        _("offered services"),
        max_length=255,
    )

    limit = models.Q(app_label="business", model="Business") | models.Q(
        app_label="client", model="ParticularClient"
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit,
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey("content_type", "object_id")

    whatsapp = PhoneNumberField(_("whatsapp"), blank=True)

    class Meta:
        app_label = "client"
        db_table = "clients"
        verbose_name = _("client")
        verbose_name_plural = _("clients")

    def __str__(self):
        return f"Client #{self.id}"

    @property
    def type(self) -> Union[Literal["business"], Literal["particular"]]:
        return (
            "particular"
            if isinstance(self.content_object, ParticularClient)
            else "business"
        )


class Social(models.Model):

    name = models.CharField(
        _("social name"),
        max_length=255,
    )

    value = models.CharField(
        _("social value"),
        max_length=255,
    )

    client = models.ForeignKey(
        "client.CommonClient",
        on_delete=models.CASCADE,
        verbose_name=_("Client"),
        related_name="socials",
    )

    class Meta:
        app_label = "client"
        db_table = "socials"
        verbose_name = _("Social")
        verbose_name_plural = _("Socials")

    def __str__(self):
        return f"{self.name} : {self.value}"


class ParticularClient(models.Model):

    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("User"),
    )

    type = models.CharField(
        _("type"),
        max_length=255,
    )

    company = models.CharField(
        _("company"),
        max_length=255,
    )

    client = GenericRelation(Client)

    @property
    def get_client(self):
        return self.client.first()

    class Meta:
        app_label = "client"
        db_table = "particular_clients"
        verbose_name = _("particular client")
        verbose_name_plural = _("particular clients")

    def __str__(self):
        return f"Particular Client {self.user}"
