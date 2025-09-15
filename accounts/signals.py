from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from .models import CustomUser

@receiver(user_logged_in)
def set_user_online(sender, request, user, **kwargs):
    """
    Set the user as online when they log in.
    """
    user.is_online = True
    user.save(update_fields=['is_online'])  # only update this field

@receiver(user_logged_out)
def set_user_offline(sender, request, user, **kwargs):
    """
    Set the user as offline when they log out.
    """
    user.is_online = False
    user.save(update_fields=['is_online'])
