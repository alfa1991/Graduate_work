# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\serializers.py



from .models import Item  # Импортируем модель Item для использования в сериализаторе
from .models import RelatedModel  # Убедитесь, что вы импортируете нужную модель
from rest_framework import serializers  # Импортируем serializers из Django REST Framework

class RelatedModelSerializer(serializers.ModelSerializer):  # Создаем сериализатор для RelatedModel
    class Meta:
        model = RelatedModel  # Указываем модель, для которой будет создан сериализатор
        fields = '__all__'  # Указываем, что нужно сериализовать все поля модели


class ItemSerializer(serializers.ModelSerializer):  # Создаем сериализатор для модели Item
    short_description = serializers.SerializerMethodField()  # Создаем поле для короткого описания
    related_model = RelatedModelSerializer(many=True, read_only=True)  # Вложенный сериализатор для связанных моделей

    class Meta:
        model = Item  # Указываем модель, для которой будет создан сериализатор
        fields = '__all__'  # Или перечислите поля явно, чтобы указать, какие поля нужно сериализовать
        read_only_fields = ['created_at', 'updated_at']  # Пример полей, которые будут только для чтения

    def get_short_description(self, obj):  # Метод для получения короткого описания
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description  # Возвращаем первые 50 символов описания, добавляя "..." если длина больше 50

    def validate_name(self, value):  # Метод для валидации поля имени
        if not value:  # Проверяем, что имя не пустое
            raise serializers.ValidationError("Имя не должно быть пустым.")  # Вызываем ошибку, если имя пустое
        return value  # Возвращаем валидированное значение
