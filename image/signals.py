from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import FarmHistory


@receiver(post_delete, sender=FarmHistory)
def delete_activity_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)
