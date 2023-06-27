from django.apps import AppConfig


class ElvatorWorklowConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elevator_worklow'

    def ready(self) -> None:
        return super().ready()
