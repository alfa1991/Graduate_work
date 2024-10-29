# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\detection_site\asgi.py

import os  # Импортируем модуль os для работы с файловой системой
from django.core.asgi import get_asgi_application  # Импортируем функцию для получения ASGI-приложения

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'detection_site.settings')  # Устанавливаем модуль настроек

# Получение ASGI-приложения
application = get_asgi_application()  # Инициализируем ASGI-приложение
