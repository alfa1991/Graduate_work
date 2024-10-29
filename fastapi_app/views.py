# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\views.py

from fastapi import APIRouter, HTTPException
from typing import List
from models import Item  # Импортируем модель Item, представляющую структуру данных для товаров

# Создаем маршрутизатор для управления запросами, связанными с товарами
item_router = APIRouter()

# Список для хранения товаров в памяти (в качестве примера данных)
items_db = []

@item_router.get("/items/", response_model=List[Item])  # Определяем маршрут для получения списка всех товаров
async def get_items():
    return items_db  # Возвращаем все товары из списка

@item_router.get("/items/{item_id}", response_model=Item)  # Определяем маршрут для получения товара по ID
async def get_item(item_id: int):
    # Пытаемся найти товар по идентификатору
    item = next((item for item in items_db if item.id == item_id), None)
    if item is None:  # Если товар не найден, возвращаем ошибку 404
        raise HTTPException(status_code=404, detail="Item not found")
    return item  # Если товар найден, возвращаем его

@item_router.post("/items/", response_model=Item)  # Определяем маршрут для создания нового товара
async def create_item(item: Item):
    items_db.append(item)  # Добавляем новый товар в список
    return item  # Возвращаем созданный товар

@item_router.put("/items/{item_id}", response_model=Item)  # Определяем маршрут для обновления товара по ID
async def update_item(item_id: int, updated_item: Item):
    # Ищем товар по идентификатору и обновляем, если найден
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item  # Возвращаем обновленный товар
    # Если товар не найден, возвращаем ошибку 404
    raise HTTPException(status_code=404, detail="Item not found")

@item_router.delete("/items/{item_id}")  # Определяем маршрут для удаления товара по ID
async def delete_item(item_id: int):
    # Ищем товар по идентификатору и удаляем, если найден
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"detail": "Item deleted"}  # Возвращаем сообщение об успешном удалении
    # Если товар не найден, возвращаем ошибку 404
    raise HTTPException(status_code=404, detail="Item not found")