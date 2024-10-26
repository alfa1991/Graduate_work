# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\init_db.py

from database import init_db
from models import User, db

from app import app  # Переместите этот импорт после определения функций, чтобы избежать циклического импорта

with app.app_context():
    init_db()  # Инициализация базы данных
    # Добавление пользователей
    user1 = User(username='Alice', age=30)
    user2 = User(username='Bob', age=25)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()  # Сохраняем изменения
