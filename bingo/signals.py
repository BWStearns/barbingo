from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

from models import BarAdministration


@receiver(post_save, sender=BarAdministration)
def grant_permissions(sender, instance, using, **kwargs):
    pass


@receiver(post_delete, sender=BarAdministration)
def revoke_permissions(sender, instance, using, **kwargs):
    pass
