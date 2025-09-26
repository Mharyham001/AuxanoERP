from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'erp_1_0'

    def ready(self):
        import erp_1_0.signals  # Import signals so Django registers them
