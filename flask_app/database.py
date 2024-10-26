# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    db.create_all()
