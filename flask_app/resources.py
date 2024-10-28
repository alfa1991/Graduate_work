from flask_restful import Resource
from flask import request
from models import User, db


class HomeResource(Resource):
    def get(self):
        return {
            "message": "Добро пожаловать в API! Используйте '/api/register' для регистрации пользователя."
        }


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

    def post(self):
        data = request.get_json()
        if not data:
            return {"message": "Неправильный формат данных."}, 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return {"message": "Все поля обязательны для заполнения."}, 400

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "Пользователь успешно зарегистрирован."}, 201

    def patch(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()

        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'password' in data:
            user.password = data['password']

        db.session.commit()
        return {"message": "Пользователь успешно обновлён."}, 200

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "Пользователь успешно удалён."}, 204

    def head(self, user_id):
        user = User.query.get(user_id)
        if user is None:
            return '', 404
        return '', 200

    def options(self):
        return {
            "methods": ["GET", "POST", "PATCH", "DELETE", "HEAD", "OPTIONS"]
        }, 200


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]


class UserRegistrationResource(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return {"message": "Неправильный формат данных."}, 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return {"message": "Все поля обязательны для заполнения."}, 400

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "Пользователь успешно зарегистрирован."}, 201
