# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\app.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources import UserResource, UserListResource, UserRegistrationResource, HomeResource

# Создаем экземпляр приложения Flask
app = Flask(__name__)

# Настройка конфигурации базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Замените на ваш URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Отключаем слежение за изменениями в базе данных

# Инициализация базы данных
db = SQLAlchemy(app)

# Инициализация API
api = Api(app)

# Добавляем ресурсы к API
api.add_resource(HomeResource, '/')  # Ресурс для приветственного сообщения
api.add_resource(UserResource, '/api/users/<int:user_id>')  # Ресурс для работы с конкретным пользователем
api.add_resource(UserListResource, '/api/users')  # Ресурс для работы со списком пользователей
api.add_resource(UserRegistrationResource, '/api/register')  # Ресурс для регистрации нового пользователя

# Главный блок запуска приложения
if __name__ == '__main__':
    # Создаем таблицы в базе данных, если они еще не существуют
    with app.app_context():
        db.create_all()
    # Запускаем приложение в режиме отладки
    app.run(debug=True)

