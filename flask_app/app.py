# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\app.py


# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Укажите правильный URI для базы данных
db = SQLAlchemy(app)  # Инициализация базы данных с приложением

# Импортируйте модели здесь
from models import User  # Убедитесь, что у вас есть этот импорт

# Создание таблиц при первом запуске приложения
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

import logging

@app.before_first_request
def log_routes():
    for rule in app.url_map.iter_rules():
        print(f"Route: {rule.endpoint} - Methods: {list(rule.methods)}")





# Для запуска:python app.py
