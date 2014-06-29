from django.dispatch import receiver
from django.db.models.signals import post_save

from models import *

@receiver(post_save.connect, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):
    if created:  
       profile, created = Account.objects.get_or_create(user=instance)

