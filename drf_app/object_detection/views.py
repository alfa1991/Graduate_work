# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item  # Импортируйте вашу модель предмета
from .serializers import ItemSerializer  # Импортируйте сериализатор предмета
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include  # Импортируйте path и include

# def index(request):
#     return HttpResponse("Hello, world!")  # Простая проверка

def home(request):
    return render(request, 'object_detection/home.html')  # Отображает шаблон home.html

def index(request):
    return render(request, 'object_detection/home.html')  # Здесь указываем, что отображается home.html


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()  # Запрос всех предметов
    serializer_class = ItemSerializer  # Сериализатор для предметов

# Убедитесь, что роутер настроен правильно
router = DefaultRouter()
router.register(r'items', ItemViewSet)  # Исправлено на ItemViewSet

urlpatterns = [
    path('', index, name='index'),  # Главная страница вашего приложения
    path('home/', home, name='home'),  # Страница "Home"
    #path('items/api/', item_list_api, name='item_list_api'),  # API для отображения списка предметов
    path('api/', include(router.urls)),  # URL для API
]

