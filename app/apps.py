from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.firebase_db_models.BigAutoField'
    name = 'app'
