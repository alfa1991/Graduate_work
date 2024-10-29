# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\config.py


# Определяем класс `Config`, который будет хранить конфигурационные параметры для приложения

class Config:
    # Указываем URI базы данных SQLite; база данных будет храниться в файле `users.db`
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Используем SQLite для простоты

    # Отключаем слежение за изменениями в базе данных для повышения производительности
    SQLALCHEMY_TRACK_MODIFICATIONS = False
