from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save

from models import BarAdministration, SquareOnCard


@receiver(post_save, sender=BarAdministration)
def grant_permissions(sender, instance, using, **kwargs):
    pass


@receiver(post_delete, sender=BarAdministration)
def revoke_permissions(sender, instance, using, **kwargs):
    pass


# Change to custom post-found-signal
@receiver(post_save, sender=SquareOnCard)
def check_for_wins(sender, instance, using, **kwargs):
    if instance.card.check_for_wins() and instance.status == "F":
        instance.card.game.declare_winner(instance.card.user)
