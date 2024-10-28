# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\urls.py

from django.urls import path, include
from .views import home, index  # Импортируем home
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', index, name='index'),  # Главная страница вашего приложения
    path('home/', home, name='home'),  # Страница "Home"
    path('api/', include(router.urls)),  # URL для API, теперь включается только router
]
