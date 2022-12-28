from django.apps import AppConfig


class PerfisAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfis_app'

    def ready(self):
        import perfis_app.signals