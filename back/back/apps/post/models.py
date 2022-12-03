from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class ContactSeller(models.Model):

    data = models.JSONField(
        _("json data for contact"),
    )

    class Meta:
        app_label = "post"
        db_table = "contact_sellers"
        verbose_name = _("contact seller")
        verbose_name_plural = _("contact sellers")

    def __str__(self):
        return self.data


class DayOption(models.Model):
    option = models.CharField(
        _("option"),
        max_length=128,
        primary_key=True,
    )

    class Meta:
        app_label = "post"
        db_table = "day_options"
        verbose_name = _("day option")
        verbose_name_plural = _("day options")

    def __str__(self):
        return self.option


class Contact(models.Model):
    first_name = models.CharField(
        _("first name"),
        max_length=255,
    )

    last_name = models.CharField(
        _("last name"),
        max_length=255,
    )

    email = models.EmailField(
        _("email"),
    )

    phone = PhoneNumberField(
        _("phone"),
    )

    local_phone = PhoneNumberField(
        _("local phone"),
    )

    contact_days = models.ManyToManyField(
        "post.DayOption",
    )

    contact_hour_start = models.DateTimeField(
        _("hour start"),
    )

    contact_hour_end = models.DateTimeField(
        _("hour end"),
    )

    class Meta:
        app_label = "post"
        db_table = "contacts"
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return f"contact for {self.first_name} {self.last_name}"


class Post(models.Model):

    author = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("author"),
    )

    address = models.ForeignKey(
        "address.Address",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("address"),
    )

    contact = models.OneToOneField(
        "post.Contact",
        on_delete=models.CASCADE,
        related_name="post",
        verbose_name=_("contact"),
    )

    details = models.TextField(
        _("details"),
    )

    media = models.ManyToManyField(
        "media.Media",
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
        app_label = "post"
        db_table = "posts"
        verbose_name = _("post")
        verbose_name_plural = _("posts")
        ordering = ("date_updated",)

    def __str__(self):
        out = [
            "post from",
            self.author,
        ]
        return " ".join([f"{o}" for o in out if o])
