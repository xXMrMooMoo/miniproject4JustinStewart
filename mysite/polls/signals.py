from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(user_logged_in)
def update_profile_on_login(sender, request, user, **kwargs):
    profile, created = Profile.objects.get_or_create(user=user)
    profile.login_count += 1
    profile.last_login = now()
    profile.save()