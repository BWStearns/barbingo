from django.dispatch import receiver
from django.core.signals import pre_delete, post_save

@receiver(post_save, sender=BarAdministration)
def grant_permissions(sender, instance, using, **kwargs):
    