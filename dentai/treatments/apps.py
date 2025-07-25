# treatments/apps.py

from django.apps import AppConfig

class TreatmentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'treatments'

    def ready(self):
        import treatments.signals
