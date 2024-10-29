# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\detection_site\wsgi.py


import os  # Импортируем модуль os для работы с переменными окружения
import logging  # Импортируем модуль logging для логирования ошибок
from django.core.wsgi import get_wsgi_application  # Импортируем функцию для создания WSGI-приложения

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'detection_site.settings')  # Устанавливаем настройки Django из модуля detection_site.settings

try:
    application = get_wsgi_application()  # Получаем WSGI-приложение
except Exception as e:  # Обрабатываем исключения, возникающие при инициализации
    logging.error("Error initializing WSGI application: %s", e)  # Логируем ошибку
    raise  # Поднимаем исключение дальше

# Получение WSGI-приложения
application = get_wsgi_application()  # Вновь получаем WSGI-приложение (можно убрать, так как уже получено выше)
