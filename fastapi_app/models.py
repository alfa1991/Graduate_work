# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\models.py

from pydantic import BaseModel  # Импортируем класс BaseModel из библиотеки Pydantic для создания моделей данных

class Item(BaseModel):  # Определяем класс Item, который будет наследовать свойства BaseModel
    id: int  # Поле id, тип данных - целое число (int)
    name: str  # Поле name, тип данных - строка (str)
    description: str  # Поле description, тип данных - строка (str)
