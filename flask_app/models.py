# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\models.py

# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'  # Убедитесь, что имя таблицы совпадает с используемым в запросе
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
