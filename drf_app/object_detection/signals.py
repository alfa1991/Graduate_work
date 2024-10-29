# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\signals.py

from django.db.models.signals import post_save  # Импортируем сигнал post_save для отслеживания сохранения модели
from django.dispatch import receiver  # Импортируем декоратор receiver для обработки сигналов
from .models import Item  # Импортируем модель Item

@receiver(post_save, sender=Item)  # Связываем сигнал post_save с моделью Item
def item_saved(sender, instance, created, **kwargs):  # Функция-обработчик сигнала
    if created:  # Проверяем, был ли создан новый объект
        print(f'Item created: {instance}')  # Выводим сообщение о создании элемента
    else:  # Если объект был обновлен
        print(f'Item updated: {instance}')  # Выводим сообщение об обновлении элемента
