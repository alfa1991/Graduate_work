# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\database.py

# Импортируем класс `SQLAlchemy` из пакета `flask_sqlalchemy`, который предоставляет инструменты для работы с базой данных
from flask_sqlalchemy import SQLAlchemy

# Создаем экземпляр `SQLAlchemy`, который будет управлять подключением к базе данных, создавать и управлять таблицами и выполнять запросы
db = SQLAlchemy()
