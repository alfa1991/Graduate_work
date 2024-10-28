# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\app.py

import logging
import os
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# # Определите директорию для логов
# log_dir = 'logs'
# os.makedirs(log_dir, exist_ok=True)  # Создание директории, если она не существует
#
# # Настройка логирования с указанием пути к файлу
# log_file = os.path.join(log_dir, 'app.log')
# logging.basicConfig(filename=log_file, level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/register', methods=['GET', 'POST'])
def register():
    from models import User  # Переместите импорт сюда, чтобы избежать циклического импорта
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = User(username=username, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/')
def index():
    return "Добро пожаловать на главную страницу!"

# Создание таблиц
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)




# Для запуска:python app.py
