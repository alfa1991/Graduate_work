# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\views.py

from flask import render_template, request, redirect, url_for
from models import User, db

def get_app():
    from app import app  # Импортируем app внутри функции
    return app

@app.route('/register_user', methods=['GET', 'POST'])  # Изменено имя маршрута
def register_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))  # Перенаправление на главную страницу
    return render_template('register.html')  # Отображаем страницу регистрации

@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/register', methods=['GET', 'POST'])  # Изменено на '/register'
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))  # Перенаправление на главную страницу
    return render_template('register.html')  # Отображаем страницу регистрации


