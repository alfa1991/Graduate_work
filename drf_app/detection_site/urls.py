# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\detection_site\urls.py

from django.contrib import admin  # Импортируем административный интерфейс Django
from django.urls import path, include  # Импортируем функции для определения URL-адресов
from django.conf import settings  # Импортируем настройки проекта
from django.conf.urls.static import static  # Импортируем функцию для обработки статических файлов

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для административной панели
    path('', include('object_detection.urls')),  # Включение URL для приложения object_detection
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Обработка статических файлов, таких как изображения
