# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item  # Импортируйте вашу модель предмета
from .serializers import ItemSerializer  # Импортируйте сериализатор предмета
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.routers import DefaultRouter
from django.urls import path, include  # Импортируйте path и include

# def index(request):
#     return HttpResponse("Hello, world!")  # Простая проверка

def home(request):
    return render(request, 'object_detection/home.html')  # Отображает шаблон home.html

def index(request):
    return render(request, 'object_detection/home.html')  # Здесь указываем, что отображается home.html

class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemDetailView(APIView):
    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = Item.objects.get(pk=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

