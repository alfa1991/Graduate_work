# object_detection/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item  # Импортируйте вашу модель предмета
from .serializers import ItemSerializer  # Импортируйте сериализатор предмета
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from django.http import HttpResponse
from django.urls import path, include  # Импортируйте path и include

def index(request):
    return HttpResponse("Hello, world!")  # Простая проверка

def home(request):
    return render(request, 'object_detection/home.html')  # Отображение главной страницы

@api_view(['GET'])
def item_list_api(request):
    items = Item.objects.all()  # Получаем все предметы
    serializer = ItemSerializer(items, many=True)  # Сериализация предметов
    return Response(serializer.data)  # Возвращаем данные в формате JSON

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # Запрос всех предметов
    serializer_class = ItemSerializer  # Сериализатор для предметов

# Убедитесь, что роутер настроен правильно
router = DefaultRouter()
router.register(r'items', ItemViewSet)  # Исправлено на ItemViewSet

urlpatterns = [
    path('', index, name='index'),  # Главная страница вашего приложения
    path('home/', home, name='home'),  # Страница "Home"
    path('items/api/', item_list_api, name='item_list_api'),  # API для отображения списка предметов
    path('api/', include(router.urls)),  # URL для API
]

