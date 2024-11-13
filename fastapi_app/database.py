# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL для подключения к базе данных SQLite (измените на путь к вашей базе данных)
DATABASE_URL = "sqlite:///./test.db"

# Создание движка SQLAlchemy
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создание объекта SessionLocal для работы с сессиями
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
