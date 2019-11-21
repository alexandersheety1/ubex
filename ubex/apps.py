from django.apps import AppConfig
from rest_framework import serializers, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import routers
from django.apps import apps
from django.urls import path, include
from django.conf import settings
from rest_framework.pagination import LimitOffsetPagination
import importlib

class ubex_config(AppConfig):
    name = 'ubex'

    def ready(self):
        # создаем роутер
        router = routers.DefaultRouter()

        # получаем модели
        list_models = apps.get_models()

        for m in list_models:
            # класс сериализатора
            class BaseSerializer(serializers.ModelSerializer):
                class Meta:
                    model = m
                    fields = '__all__'

            # класс представление
            class BaseViewSet(viewsets.ModelViewSet):
                # поддержка методов
                http_method_names = ['get', 'post', 'put', 'delete']

                # бэкенды фильрации и сортировки
                filter_backends = [DjangoFilterBackend, OrderingFilter]

                # поддержка фильтрации по всем полям
                filterset_fields = '__all__'

                # поддержка сериализации всех полей модели
                serializer_class = BaseSerializer

                queryset = m.objects.all()

                # поддежка команды limit в GET запросе
                pagination_class = LimitOffsetPagination

            name = m.__name__.replace(" ", "").lower()

            # регистрируем представление
            router.register(
                name,
                BaseViewSet,
                basename=name,
            )

        # подключаем урлы к главным урлам
        urlpatterns = importlib.import_module(settings.ROOT_URLCONF).urlpatterns
        urlpatterns.append(path('', include(router.urls)))

