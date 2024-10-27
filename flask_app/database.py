# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)  # Привязываем SQLAlchemy к приложению Flask
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных