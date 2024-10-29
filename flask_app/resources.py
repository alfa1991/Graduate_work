# Импортируем Resource из flask_restful, чтобы создавать RESTful ресурсы (классы для обработки API-запросов).
from flask_restful import Resource
# Импортируем request из flask для получения данных из запроса.
from flask import request
# Импортируем модели User и db (база данных) из файла models для работы с пользователями в БД.
from models import User, db

# Определяем ресурс HomeResource для обработки запроса к главной странице API.
class HomeResource(Resource):
    # Метод get() для обработки GET-запроса к главной странице.
    def get(self):
        # Возвращаем приветственное сообщение и указание для регистрации пользователя.
        return {
            "message": "Добро пожаловать в API! Используйте '/api/register' для регистрации пользователя."
        }

# Определяем ресурс UserResource для работы с конкретным пользователем.
class UserResource(Resource):
    # Метод get() для получения информации о пользователе по ID.
    def get(self, user_id):
        # Ищем пользователя в базе данных по ID. Если пользователь не найден, возвращается ошибка 404.
        user = User.query.get_or_404(user_id)
        # Возвращаем данные пользователя в виде JSON-объекта.
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

    # Метод post() для создания нового пользователя.
    def post(self):
        # Получаем данные JSON из запроса.
        data = request.get_json()
        # Если данные не переданы, возвращаем ошибку 400.
        if not data:
            return {"message": "Неправильный формат данных."}, 400

        # Получаем значения username, email и password из данных.
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Проверяем, что все поля заполнены. Если нет, возвращаем ошибку.
        if not username or not email or not password:
            return {"message": "Все поля обязательны для заполнения."}, 400

        # Создаем нового пользователя и добавляем его в сессию базы данных.
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        # Сохраняем изменения в базе данных.
        db.session.commit()

        # Возвращаем сообщение о успешной регистрации.
        return {"message": "Пользователь успешно зарегистрирован."}, 201

    # Метод patch() для обновления данных пользователя по ID.
    def patch(self, user_id):
        # Ищем пользователя в базе данных по ID.
        user = User.query.get_or_404(user_id)
        # Получаем данные JSON из запроса.
        data = request.get_json()

        # Обновляем поля пользователя, если они переданы в запросе.
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']

        # Сохраняем изменения в базе данных.
        db.session.commit()
        # Возвращаем сообщение об успешном обновлении.
        return {"message": "Пользователь успешно обновлён."}, 200

    # Метод delete() для удаления пользователя по ID.
    def delete(self, user_id):
        # Ищем пользователя в базе данных по ID.
        user = User.query.get_or_404(user_id)
        # Удаляем пользователя из базы данных.
        db.session.delete(user)
        # Сохраняем изменения.
        db.session.commit()
        # Возвращаем сообщение об успешном удалении.
        return {"message": "Пользователь успешно удалён."}, 204

    # Метод head() для проверки наличия пользователя по ID.
    def head(self, user_id):
        # Проверяем, существует ли пользователь. Если нет, возвращаем 404.
        user = User.query.get(user_id)
        if user is None:
            return '', 404
        # Если пользователь найден, возвращаем 200 без тела ответа.
        return '', 200

    # Метод options() для возвращения доступных методов.
    def options(self):
        return {
            "methods": ["GET", "POST", "PATCH", "DELETE", "HEAD", "OPTIONS"]
        }, 200

# Определяем ресурс UserListResource для работы со списком пользователей.
class UserListResource(Resource):
    # Метод get() для получения списка всех пользователей.
    def get(self):
        # Получаем всех пользователей из базы данных.
        users = User.query.all()
        # Возвращаем список пользователей в формате JSON.
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]

# Определяем ресурс UserRegistrationResource для регистрации нового пользователя.
class UserRegistrationResource(Resource):
    # Метод get() для отображения информации о необходимости использовать POST для регистрации.
    def get(self):
        return {"message": "Для регистрации пользователя используйте метод POST."}, 200

    # Метод post() для создания нового пользователя.
    def post(self):
        # Получаем данные JSON из запроса.
        data = request.get_json()
        # Если данные не переданы, возвращаем ошибку 400.
        if not data:
            return {"message": "Неправильный формат данных."}, 400

        # Получаем значения username, email и password из данных.
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Проверяем, что все поля заполнены. Если нет, возвращаем ошибку.
        if not username or not email or not password:
            return {"message": "Все поля обязательны для заполнения."}, 400

        # Создаем нового пользователя и добавляем его в сессию базы данных.
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        # Сохраняем изменения в базе данных.
        db.session.commit()

        # Возвращаем сообщение о успешной регистрации.
        return {"message": "Пользователь успешно зарегистрирован."}, 201
