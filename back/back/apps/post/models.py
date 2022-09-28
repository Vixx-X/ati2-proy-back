from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


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

    class Meta:
        app_label = "post"
        db_table = "contacts"
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")

    def __str__(self):
        return ""


class Post(models.Model):

    author = models.ForeignKey(
        "client.Client",
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name=_("author"),
    )

    address = models.ForeignKey(
        "adress.Address",
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
        abstract = True
        app_label = "post"
        db_table = "posts"
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self):
        out = [
            "post from",
            self.author,
        ]
        return " ".join([f"{o}" for o in out if o])
