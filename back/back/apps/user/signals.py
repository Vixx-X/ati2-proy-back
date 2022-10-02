from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from back.apps.user.mails import WelcomeMail
from .models import User, EmailDevice

user_registered = Signal()


@receiver(post_save, sender=User)
def creating_user_settings(sender, instance, created, raw, **kwargs):
    """Creating the user device for a new User"""

    if created and not raw:
        EmailDevice.objects.create(
            user=instance,
            name=f"personal device for user {instance.pk}",
            confirmed=True,
        )


@receiver(user_registered, sender=User)
def user_registered_callback(sender, instance, created, raw, **kwargs):
    """Send user registration email"""

    user = instance
    context = {user: user}

    mail = WelcomeMail()
    mail.set_context(**context)
    mail.send([user.email])
