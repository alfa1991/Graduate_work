# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\admin.py

from django.contrib import admin
from .models import Item  # Импортируем модель Item для работы с ней в админке

@admin.register(Item)  # Регистрируем модель Item в админке
class ItemAdmin(admin.ModelAdmin):
    # Определяем поля, которые будут отображаться в списке объектов
    list_display = ('name', 'description', 'image', 'get_related_price')  # Отображаем поля имени, описания, изображения и цены

    # Добавляем фильтры для удобства поиска и сортировки
    list_filter = ('category', 'created_at')  # Позволяет фильтровать элементы по категории и дате создания

    search_fields = ('name',)  # Позволяет искать элементы по имени

    ordering = ('-created_at',)  # Сортировка по дате создания в обратном порядке (новейшие первыми)

    readonly_fields = ('created_at',)  # Указываем поля только для чтения (например, дата создания)

    fields = ('name', 'description', 'image', 'category', 'price')  # Поля для редактирования в форме

    # Метод для получения цен связанных элементов
    def get_related_price(self, obj):
        # Получаем цены всех связанных элементов
        related_prices = [related.price for related in obj.related_items.all()]
        # Возвращаем строки цен или сообщение, если цен нет
        return ', '.join(map(str, related_prices)) if related_prices else 'Нет цены'

    # Название столбца для отображения цены в админке
    get_related_price.short_description = 'Цена'
