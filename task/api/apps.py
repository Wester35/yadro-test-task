import threading
from django.db.utils import OperationalError
from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from .load_users import get_users_from_api
        threading.Thread(target=get_users_from_api, daemon=True).start()