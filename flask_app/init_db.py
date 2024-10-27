# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\init_db.py

from app import app
from database import db

# Инициализация базы данных и создание таблиц
with app.app_context():
    db.create_all()
    print("База данных успешно инициализирована.")