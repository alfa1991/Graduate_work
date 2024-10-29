# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\models.py



from django.db import models  # Импортируем модуль models из Django для создания моделей базы данных

class Item(models.Model):  # Определяем модель Item, представляющую предмет
    name = models.CharField(max_length=255)  # Название предмета, ограниченное 255 символами
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена предмета с 10 цифрами всего и 2 после запятой
    category = models.CharField(max_length=255, blank=True, null=True)  # Категория предмета, допускающая пустые значения
    description = models.TextField()  # Описание предмета, позволяющее вводить большой объем текста
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)  # Дата создания предмета, автоматически заполняемая при создании
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего обновления предмета, автоматически обновляется
    is_available = models.BooleanField(default=True)  # Статус доступности предмета, по умолчанию доступен
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)  # Поле для загрузки изображения предмета

    def get_short_description(self):  # Метод для получения короткого описания предмета
        """Получить короткое описание предмета."""
        return self.description[:50] + '...' if len(self.description) > 50 else self.description  # Возвращаем первые 50 символов описания с добавлением "..." если оно длиннее

    def __str__(self):  # Метод, возвращающий строковое представление предмета
        return self.name  # Возвращаем имя предмета


class RelatedModel(models.Model):  # Определяем модель RelatedModel, связанной с Item
    item = models.ForeignKey(Item, related_name='related_items', on_delete=models.CASCADE)  # Внешний ключ, указывающий на связанный предмет
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена связанной модели с 10 цифрами всего и 2 после запятой
    size = models.CharField(max_length=50, blank=True, null=True)  # Размер предмета, допускающий пустые значения

    def __str__(self):  # Метод, возвращающий строковое представление связанной модели
        return f"{self.item.name} - {self.price} - {self.size}"  # Возвращаем строку с информацией о предмете и его цене

