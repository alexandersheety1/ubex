from django.apps import AppConfig


class Core2Config(AppConfig):
    name = 'core2'

    def ready(self):
        g=10
