# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\urls.py

from django.urls import path, include  # Импортируем функции path и include для определения маршрутов
from .views import home, index  # Импортируем представления home и index из текущего приложения
from rest_framework.routers import DefaultRouter  # Импортируем DefaultRouter для создания маршрутов API
from .views import ItemViewSet, ItemListView, ItemDetailView  # Импортируем ItemViewSet для работы с элементами

router = DefaultRouter()  # Создаем экземпляр маршрутизатора
router.register(r'items', ItemViewSet)  # Регистрируем ItemViewSet под URL 'items'

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('', index, name='index'),  # Определяем маршрут для главной страницы приложения
    path('home/', home, name='home'),  # Определяем маршрут для страницы "Home"
    path('api/', include(router.urls)),  # Включаем маршруты API, определенные в router
]
