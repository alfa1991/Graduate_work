# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\database.py

# Импортируем необходимые классы и функции из SQLAlchemy
from sqlalchemy import create_engine  # create_engine создает объект подключения к базе данных
from sqlalchemy.ext.declarative import declarative_base  # declarative_base позволяет создать базовый класс для моделей
from sqlalchemy.orm import sessionmaker  # sessionmaker создает фабрику для создания сессий

# URL для подключения к базе данных SQLite
# "sqlite:///./test.db" указывает, что используется база данных SQLite и файл базы данных находится в текущем каталоге под именем "test.db"
DATABASE_URL = "sqlite:///./test.db"

# Создание движка SQLAlchemy
# create_engine создает движок, который управляет подключениями к базе данных
# connect_args={"check_same_thread": False} используется только для SQLite и разрешает использовать базу данных в разных потоках
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создание объекта SessionLocal для работы с сессиями
# sessionmaker создает фабрику для объектов сессий, которые используются для взаимодействия с базой данных
# autocommit=False — отключает автокоммит, изменения нужно явно фиксировать вызовом commit()
# autoflush=False — отключает автоматическую отправку изменений в базу перед выполнением запросов
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
# Base используется для создания ORM-классов (моделей) на основе SQLAlchemy
# Все модели будут наследоваться от этого класса, чтобы автоматически связаться с таблицами базы данных
Base = declarative_base()

# Функция для получения сессии базы данных
# get_db — это генератор, который предоставляет объект сессии и затем закрывает его после использования
# Это помогает управлять подключениями к базе данных и предотвращает утечки памяти
def get_db():
    db = SessionLocal()  # Создаем объект сессии
    try:
        yield db  # Возвращаем сессию для использования в зависимости (dependency)
    finally:
        db.close()  # Закрываем сессию после завершения работы
