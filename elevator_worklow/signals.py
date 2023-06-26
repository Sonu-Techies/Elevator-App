from django.db.models.signals import post_save
from django.dispatch import receiver

from elevator_worklow.models import Elevator, Floor

@receiver(post_save, sender=Elevator)
def create_floor(instance, **kwargs):
    """
    Create Offer when elevator instance is created
    """

    if kwargs["created"]:
        Floor.objects.create(
            elevator=instance,
            floor_number=0
        )

