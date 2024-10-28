# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\models.py



from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)  # Название предмета
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, blank=True, null=True)  # Сделать поле nullable
    description = models.TextField()  # Описание предмета
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Сделать поле nullable
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления
    is_available = models.BooleanField(default=True)  # Статус доступности
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)  # Поле для изображения

    def get_short_description(self):
        """Получить короткое описание предмета."""
        return self.description[:50] + '...' if len(self.description) > 50 else self.description

    def __str__(self):
        return self.name


class RelatedModel(models.Model):
    item = models.ForeignKey(Item, related_name='related_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Пример дополнительного поля
    size = models.CharField(max_length=50, blank=True, null=True)  # Размер предмета

    def __str__(self):
        return f"{self.item.name} - {self.price} - {self.size}"

