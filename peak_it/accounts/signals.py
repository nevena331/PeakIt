from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import update_last_login


@receiver(post_save, sender=Token)
def update_last_login_on_token(sender, instance, **kwargs):
    print("update last login")
    update_last_login(None, instance.user)