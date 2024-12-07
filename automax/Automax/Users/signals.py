from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Profile,Location


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)  # 'user' should match the field name in Profile model


@receiver(post_save, sender=Profile)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile_location = Location.objects.create()
        instance.location= profile_location
        instance.save()


@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, **kwargs):
    if hasattr(instance, 'location') and instance.location:
        instance.location.delete()
