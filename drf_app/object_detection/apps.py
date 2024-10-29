# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\apps.py

from django.apps import AppConfig  # Импортируем AppConfig для настройки приложения

class ObjectDetectionConfig(AppConfig):  # Определяем конфигурацию приложения ObjectDetection
    default_auto_field = 'django.db.models.BigAutoField'  # Указываем тип автоинкрементного поля по умолчанию
    name = 'object_detection'  # Имя приложения
    verbose_name = 'Обнаружение объектов'  # Человеческое имя приложения для админки

    def ready(self):  # Метод, который вызывается, когда приложение готово
        import object_detection.signals  # Импортируем сигналы для регистрации обработчиков сигналов
        self.create_initial_data()  # Вызываем метод для создания начальных данных

    def create_initial_data(self):  # Метод для создания начальных данных в базе данных
        from .models import Item  # Импортируем модель Item

        # Проверка, есть ли уже данные, чтобы избежать дублирования
        if Item.objects.count() == 0:  # Если в базе данных нет предметов
            Item.objects.create(name='Пример предмета', description='Это пример описания.')  # Создаем пример предмета
            print('Начальные данные созданы.')  # Выводим сообщение в консоль о создании начальных данных
