# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\main.py

from fastapi import FastAPI, Depends # Импортируем класс FastAPI для создания приложения
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from views import item_router  # Импортируем маршрутизатор item_router из модуля views

# Создаем таблицы в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()  # Создаем экземпляр приложения FastAPI

app.include_router(item_router)  # Подключаем маршрутизатор item_router к приложению


@app.get("/")  # Обрабатываем GET-запрос на корневой маршрут
async def get_root():  # Асинхронная функция для обработки GET-запроса
    return {"message": "GET request received"}  # Возвращаем сообщение о получении GET-запроса

@app.post("/")  # Обрабатываем POST-запрос на корневой маршрут
async def post_root():  # Асинхронная функция для обработки POST-запроса
    return {"message": "POST request received"}  # Возвращаем сообщение о получении POST-запроса

@app.put("/")  # Обрабатываем PUT-запрос на корневой маршрут
async def put_root():  # Асинхронная функция для обработки PUT-запроса
    return {"message": "PUT request received"}  # Возвращаем сообщение о получении PUT-запроса

@app.patch("/")  # Обрабатываем PATCH-запрос на корневой маршрут
async def patch_root():  # Асинхронная функция для обработки PATCH-запроса
    return {"message": "PATCH request received"}  # Возвращаем сообщение о получении PATCH-запроса

@app.delete("/")  # Обрабатываем DELETE-запрос на корневой маршрут
async def delete_root():  # Асинхронная функция для обработки DELETE-запроса
    return {"message": "DELETE request received"}  # Возвращаем сообщение о получении DELETE-запроса

@app.head("/")  # Обрабатываем HEAD-запрос на корневой маршрут
async def head_root():  # Асинхронная функция для обработки HEAD-запроса
    return {"message": "HEAD request received"}  # Возвращаем сообщение о получении HEAD-запроса

@app.options("/")  # Обрабатываем OPTIONS-запрос на корневой маршрут
async def options_root():  # Асинхронная функция для обработки OPTIONS-запроса
    return {"message": "OPTIONS request received"}  # Возвращаем сообщение о получении OPTIONS-запроса


# Запуск приложения, используя uvicorn:
# uvicorn main:app --reload
