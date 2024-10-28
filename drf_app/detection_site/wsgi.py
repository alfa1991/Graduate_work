# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\detection_site\wsgi.py


import os
import logging
from django.core.wsgi import get_wsgi_application

# Установка переменной окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'detection_site.settings')

try:
    application = get_wsgi_application()
except Exception as e:
    logging.error("Error initializing WSGI application: %s", e)
    raise

# Получение WSGI-приложения
application = get_wsgi_application()
