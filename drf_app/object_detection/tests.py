# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\tests.py

from rest_framework.test import APITestCase  # Импортируем APITestCase для создания тестов API
from rest_framework import status  # Импортируем статусы HTTP
from .models import Item  # Импортируем модель Item

class ItemAPITests(APITestCase):  # Определяем класс тестов для API элементов

    def setUp(self):  # Метод, выполняющийся перед каждым тестом
        """Создание объекта Item перед каждым тестом."""  # Докстринг для описания метода
        self.item_data = {  # Данные для создания элемента
            'name': 'Test Item',  # Имя элемента
            'description': 'Test Description',  # Описание элемента
            'is_available': True,  # Доступность элемента
        }

    def test_create_item(self):  # Тест для проверки создания элемента
        """Тестирование создания элемента."""  # Докстринг для описания теста
        response = self.client.post('/api/items/', self.item_data)  # Отправляем POST-запрос для создания элемента
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверяем, что статус ответа 201 (создано)
        self.assertEqual(Item.objects.count(), 1)  # Проверяем, что в базе данных теперь 1 элемент
        self.assertEqual(Item.objects.get().name, 'Test Item')  # Проверяем, что имя созданного элемента верное

    def test_get_items(self):  # Тест для проверки получения списка элементов
        """Тестирование получения списка элементов."""  # Докстринг для описания теста
        Item.objects.create(**self.item_data)  # Создаем элемент для теста
        response = self.client.get('/api/items/')  # Отправляем GET-запрос для получения списка элементов
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверяем, что статус ответа 200 (успешно)
        self.assertEqual(len(response.data), 1)  # Проверяем, что один элемент вернулся

    def test_create_item_with_image(self):  # Тест для проверки создания элемента с изображением
        """Тестирование создания элемента с изображением."""  # Докстринг для описания теста
        image_path = 'C:/Users/Ilgiz Agliullin/PycharmProjects/Graduate_work/drf_app/media/images/pexels-ash-craig-122861-376464.jpg'  # Путь к изображению
        with open(image_path, 'rb') as img:  # Открываем изображение в бинарном режиме
            response = self.client.post('/api/items/', {  # Отправляем POST-запрос с изображением
                'name': 'Image Item',  # Имя элемента
                'description': 'Item with an image',  # Описание элемента
                'image': img  # Изображение элемента
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверяем, что статус ответа 201 (создано)
        self.assertEqual(Item.objects.count(), 1)  # Проверяем, что в базе данных теперь 1 элемент
        self.assertTrue(Item.objects.get().image)  # Проверяем, что изображение сохранено

    def test_create_item_missing_name(self):  # Тест для проверки создания элемента без имени
        """Тестирование создания элемента без названия."""  # Докстринг для описания теста
        response = self.client.post('/api/items/', {  # Отправляем POST-запрос с отсутствующим именем
            'description': 'Description without name'  # Описание элемента без имени
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Проверяем, что статус ответа 400 (плохой запрос)
        self.assertEqual(Item.objects.count(), 0)  # Убедимся, что элемент не был создан

    def test_item_availability(self):  # Тест для проверки доступности элемента
        """Тестирование доступности элемента."""  # Докстринг для описания теста
        item = Item.objects.create(**self.item_data, is_available=False)  # Создаем элемент с недоступностью
        response = self.client.get('/api/items/')  # Отправляем GET-запрос для получения списка элементов
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверяем, что статус ответа 200 (успешно)
        self.assertEqual(response.data[0]['is_available'], False)  # Проверяем статус доступности
