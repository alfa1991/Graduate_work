# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\views.py

from rest_framework.views import APIView  # Импортируем класс APIView из Django REST Framework для создания представлений на основе классов.
from rest_framework.response import Response  # Импортируем класс Response для формирования ответов на HTTP запросы.
from .models import Item  # Импортируем модель Item из текущего приложения, чтобы работать с предметами.
from .serializers import ItemSerializer  # Импортируем сериализатор ItemSerializer для обработки и валидации данных.
from django.shortcuts import render  # Импортируем функцию render для отображения HTML-шаблонов.
from rest_framework import viewsets, status  # Импортируем viewsets для создания представлений и status для HTTP статусов.
from rest_framework.routers import DefaultRouter  # Импортируем DefaultRouter для автоматической маршрутизации.
from django.urls import path, include  # Импортируем функции path и include для определения URL маршрутов.

# def index(request):
#     return HttpResponse("Hello, world!")  # Простая проверка, возвращающая текст "Hello, world!".

def home(request):  # Определяем функцию представления для главной страницы.
    return render(request, 'object_detection/home.html')  # Отображает шаблон home.html.

def index(request):  # Определяем функцию представления для индекса.
    return render(request, 'object_detection/home.html')  # Отображает шаблон home.html.

class ItemListView(APIView):  # Класс представления для списка предметов, наследующий от APIView.
    def get(self, request):  # Метод для обработки GET-запросов.
        items = Item.objects.all()  # Получаем все объекты Item из базы данных.
        serializer = ItemSerializer(items, many=True)  # Сериализуем объекты в формат JSON.
        return Response(serializer.data)  # Возвращаем сериализованные данные в ответе.

    def post(self, request):  # Метод для обработки POST-запросов.
        serializer = ItemSerializer(data=request.data)  # Создаем сериализатор с входными данными.
        if serializer.is_valid():  # Проверяем, валидны ли данные.
            serializer.save()  # Сохраняем объект в базе данных.
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Возвращаем сериализованные данные с кодом 201 (создано).
        print(serializer.errors)  # Выводим ошибки в консоль для отладки.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки с кодом 400 (плохой запрос).

class ItemDetailView(APIView):  # Класс представления для деталей предмета, наследующий от APIView.
    def get(self, request, pk):  # Метод для обработки GET-запросов по конкретному предмету.
        item = Item.objects.get(pk=pk)  # Получаем объект Item по первичному ключу.
        serializer = ItemSerializer(item)  # Сериализуем объект в формат JSON.
        return Response(serializer.data)  # Возвращаем сериализованные данные в ответе.

    def put(self, request, pk):  # Метод для обработки PUT-запросов для обновления предмета.
        item = self.get_object(pk)  # Получаем объект по первичному ключу с помощью метода get_object.
        serializer = ItemSerializer(item, data=request.data)  # Создаем сериализатор с новыми данными.
        if serializer.is_valid():  # Проверяем, валидны ли данные.
            serializer.save()  # Сохраняем обновленный объект в базе данных.
            return Response(serializer.data)  # Возвращаем сериализованные данные в ответе.
        print(serializer.errors)  # Выводим ошибки в консоль для отладки.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки с кодом 400 (плохой запрос).

    def delete(self, request, pk):  # Метод для обработки DELETE-запросов для удаления предмета.
        item = Item.objects.get(pk=pk)  # Получаем объект Item по первичному ключу.
        item.delete()  # Удаляем объект из базы данных.
        return Response(status=status.HTTP_204_NO_CONTENT)  # Возвращаем статус 204 (нет содержимого) в ответе.

class ItemViewSet(viewsets.ModelViewSet):  # Класс представления для предметов, наследующий от ModelViewSet.
    queryset = Item.objects.all()  # Запрос всех предметов из базы данных.
    serializer_class = ItemSerializer  # Указываем сериализатор для предметов.

# Убедитесь, что роутер настроен правильно.
router = DefaultRouter()  # Создаем экземпляр маршрутизатора по умолчанию.
router.register(r'items', ItemViewSet)  # Регистрируем ItemViewSet с маршрутом 'items'.

urlpatterns = [  # Определяем список URL-маршрутов для приложения.
    path('', index, name='index'),  # Главная страница вашего приложения, обрабатываемая функцией index.
    path('home/', home, name='home'),  # Страница "Home", обрабатываемая функцией home.
    # path('items/api/', item_list_api, name='item_list_api'),  # API для отображения списка предметов (закомментировано).
    path('api/', include(router.urls)),  # Включаем маршруты API, определенные в роутере.
]
