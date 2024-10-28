# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\detection_site\urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для административной панели
    path('', include('object_detection.urls')),  # Включение URL для приложения object_detection
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
