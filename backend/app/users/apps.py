#app/users/apps.py
from django.apps import AppConfig
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.users'
    verbose_name = 'User Management'

    def ready(self):
        import app.users.signals  # Import signals to connect them

