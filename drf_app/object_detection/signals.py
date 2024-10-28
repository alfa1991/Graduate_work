# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Item

@receiver(post_save, sender=Item)
def item_saved(sender, instance, created, **kwargs):
    if created:
        print(f'Item created: {instance}')
    else:
        print(f'Item updated: {instance}')
