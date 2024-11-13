# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\models.py

from pydantic import BaseModel  # Импортируем класс BaseModel из библиотеки Pydantic для создания моделей данных
from sqlalchemy import Column, Integer, String
from database import Base

class Item(BaseModel):  # Определяем класс Item, который будет наследовать свойства BaseModel
    id: int  # Поле id, тип данных - целое число (int)
    name: str  # Поле name, тип данных - строка (str)
    description: str  # Поле description, тип данных - строка (str)

class Item(Base):  # Класс для работы с базой данных SQLAlchemy
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)