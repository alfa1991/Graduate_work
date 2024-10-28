# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\apps.py

from django.apps import AppConfig

class ObjectDetectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'object_detection'
    verbose_name = 'Обнаружение объектов'

    def ready(self):
        import object_detection.signals  # Регистрация сигналов
        self.create_initial_data()  # Вызов метода для инициализации данных

    def create_initial_data(self):
        from .models import Item

        # Проверка, есть ли уже данные, чтобы избежать дублирования
        if Item.objects.count() == 0:
            Item.objects.create(name='Пример предмета', description='Это пример описания.')
            print('Начальные данные созданы.')