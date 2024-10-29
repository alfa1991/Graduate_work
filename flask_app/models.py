# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\models.py

# Импортируем класс SQLAlchemy для работы с базой данных
from flask_sqlalchemy import SQLAlchemy

# Создаём экземпляр SQLAlchemy для использования в приложении Flask
db = SQLAlchemy()


# Определяем модель User, которая будет представлять таблицу `user` в базе данных
class User(db.Model):
    # Указываем имя таблицы в базе данных
    __tablename__ = 'user'  # Убедитесь, что имя таблицы совпадает с используемым в запросе

    # Поле `id` - первичный ключ, уникально идентифицирующее каждого пользователя
    id = db.Column(db.Integer, primary_key=True)

    # Поле `username` - строка с максимальной длиной 80 символов, должно быть уникальным и не может быть пустым
    username = db.Column(db.String(80), unique=True, nullable=False)

    # Поле `email` - строка с максимальной длиной 120 символов, должно быть уникальным и не может быть пустым
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Поле `password` - строка с максимальной длиной 200 символов, не может быть пустым
    password = db.Column(db.String(200), nullable=False)

    # Метод `__repr__` возвращает строковое представление объекта User для удобства отладки
    def __repr__(self):
        return f'<User {self.username}>'

