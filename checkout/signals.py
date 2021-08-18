from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
<<<<<<< HEAD
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
=======
def update_on_delete(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
>>>>>>> c6b7239dec7e496cdbb40764aa6ef5b15e7ce133
    """
    instance.order.update_total()
