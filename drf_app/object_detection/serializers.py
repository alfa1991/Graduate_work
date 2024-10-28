# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\object_detection\serializers.py



from .models import Item
from .models import RelatedModel  # Убедитесь, что вы импортируете нужную модель
from rest_framework import serializers

class RelatedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedModel
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()
    related_model = RelatedModelSerializer(many=True, read_only=True)  # Вложенный сериализатор

    class Meta:
        model = Item
        fields = '__all__'  # Или перечислите поля явно
        read_only_fields = ['created_at', 'updated_at']  # Пример полей только для чтения

    def get_short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Имя не должно быть пустым.")
        return value