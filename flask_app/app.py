# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\app.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from resources import UserResource, UserListResource, UserRegistrationResource, HomeResource

app = Flask(__name__)

# Настройка конфигурации базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Замените на ваш URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db = SQLAlchemy(app)

# Инициализация API
api = Api(app)

# Добавляем ресурсы к API
api.add_resource(HomeResource, '/')
api.add_resource(UserResource, '/api/users/<int:user_id>')
api.add_resource(UserListResource, '/api/users')
api.add_resource(UserRegistrationResource, '/api/register')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создаем таблицы в базе данных, если они не существуют
    app.run(debug=True)

