# organizations/apps.py
from django.apps import AppConfig

class OrganizationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'organizations'  # Ensure this matches your app name