# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\models.py

from pydantic import BaseModel  # Импортируем класс BaseModel из библиотеки Pydantic для создания моделей данных
from sqlalchemy import Column, Integer, String
from database import Base


class Item(Base):  # Класс для работы с базой данных SQLAlchemy
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)