from django.db.models.signals import post_migrate
from django.dispatch import receiver
from api.models import User
from api.load_users import get_users_from_api

@receiver(post_migrate)
def create_initial_users(sender, **kwargs):
    if User.objects.count() == 0:
        get_users_from_api()