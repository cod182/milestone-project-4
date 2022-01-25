from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile if one doesn't exist
    Update profile if already exists
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
