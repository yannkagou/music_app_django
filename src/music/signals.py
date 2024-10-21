from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Subscriber

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_subscriber_for_new_user(sender, **kwargs):
    if kwargs["created"]:
        Subscriber.objects.create(user=kwargs["instance"])