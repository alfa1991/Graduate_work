# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\fastapi_app\models.py


from sqlalchemy import Column, Integer, String  # Импортируем нужные типы данных для определения столбцов
from database import Base  # Импортируем базовый класс Base из database.py, от которого будут наследоваться модели

# Определяем класс Item, который представляет таблицу "items" в базе данных
class Item(Base):  # Класс Item наследует Base, что позволяет SQLAlchemy работать с ним как с моделью
    __tablename__ = "items"  # Указываем имя таблицы в базе данных ("items"), которая будет соответствовать этому классу

    # Определяем столбец "id" для хранения уникального идентификатора записи
    # Column(Integer) задает тип данных Integer для столбца
    # primary_key=True указывает, что это первичный ключ таблицы, уникальный для каждой записи
    # index=True создает индекс для столбца "id", что ускоряет поиск по этому полю
    id = Column(Integer, primary_key=True, index=True)

    # Определяем столбец "name" для хранения названия объекта
    # Column(String) задает тип данных String для столбца
    # index=True создает индекс для столбца "name", что ускоряет поиск по этому полю
    name = Column(String, index=True)

    # Определяем столбец "description" для хранения описания объекта
    # Column(String) задает тип данных String для столбца, где будет храниться текстовое описание
    description = Column(String)
