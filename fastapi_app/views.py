# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\views.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from typing import List
from models import Item as ItemModel   # Импортируем модель Item, представляющую структуру данных для товаров

# Схема Pydantic для запросов и ответов
class Item(BaseModel):
    name: str
    description: str

    class Config:
        from_attributes = True  # Используем 'from_attributes'

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