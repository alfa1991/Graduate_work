# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemAPITests(APITestCase):

    def setUp(self):
        """Создание объекта Item перед каждым тестом."""
        self.item_data = {
            'name': 'Test Item',
            'description': 'Test Description',
            'is_available': True,
        }

    def test_create_item(self):
        """Тестирование создания элемента."""
        response = self.client.post('/api/items/', self.item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertEqual(Item.objects.get().name, 'Test Item')

    def test_get_items(self):
        """Тестирование получения списка элементов."""
        Item.objects.create(**self.item_data)  # Создаем элемент для теста
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Проверяем, что один элемент вернулся

    def test_create_item_with_image(self):
        """Тестирование создания элемента с изображением."""
        image_path = 'C:/Users/Ilgiz Agliullin/PycharmProjects/Graduate_work/drf_app/media/images/pexels-ash-craig-122861-376464.jpg'
        with open(image_path, 'rb') as img:
            response = self.client.post('/api/items/', {
                'name': 'Image Item',
                'description': 'Item with an image',
                'image': img
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Item.objects.count(), 1)
        self.assertTrue(Item.objects.get().image)  # Проверяем, что изображение сохранено

    def test_create_item_missing_name(self):
        """Тестирование создания элемента без названия."""
        response = self.client.post('/api/items/', {
            'description': 'Description without name'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Item.objects.count(), 0)  # Убедимся, что элемент не был создан

    def test_item_availability(self):
        """Тестирование доступности элемента."""
        item = Item.objects.create(**self.item_data, is_available=False)
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['is_available'], False)  # Проверяем статус доступности
