# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\views.py

from fastapi import APIRouter, HTTPException, Depends  # Импортируем нужные классы и функции из FastAPI
from sqlalchemy.orm import Session  # Импортируем класс Session для работы с сессиями SQLAlchemy
from database import get_db  # Импортируем функцию get_db для получения сессии базы данных
from pydantic import BaseModel  # Импортируем базовый класс для схемы данных
from typing import List  # Импортируем тип List для указания списков в аннотациях
from models import Item as ItemModel  # Импортируем модель Item из модуля models и задаем ей псевдоним ItemModel

# Создаем схему Pydantic для запросов и ответов, представляющую структуру данных для объектов типа "Item"
class Item(BaseModel):
    name: str  # Поле "name", тип данных — строка, представляет название объекта
    description: str  # Поле "description", тип данных — строка, представляет описание объекта

    # Вложенный класс Config для настройки поведения модели Pydantic
    class Config:
        from_attributes = True  # Устанавливаем from_attributes=True, чтобы разрешить преобразование из объектов SQLAlchemy в объекты Pydantic

# Создаем маршрутизатор для управления запросами, связанными с товарами
item_router = APIRouter()


# GET: Получение всех товаров
@item_router.get("/items/", response_model=List[Item])
async def get_items(db: Session = Depends(get_db)):
    return db.query(ItemModel).all()

# GET: Получение товара по ID
@item_router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# POST: Создание нового товара
@item_router.post("/items/", response_model=Item)
async def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = ItemModel(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# PUT: Обновление товара по ID
@item_router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = updated_item.name
    item.description = updated_item.description
    db.commit()
    db.refresh(item)
    return item

# DELETE: Удаление товара по ID
@item_router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"detail": "Item deleted"}