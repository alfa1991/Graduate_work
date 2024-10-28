# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\views.py

from flask import render_template, request, redirect, url_for
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from app import app

def get_app():
    from app import app  # Импортируем app внутри функции
    return app

@app.route('/')
def home():
    return render_template('index.html')  # Убедитесь, что файл home.html существует


@app.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')  # Используйте get() вместо прямого доступа
        if username and email and password:
            # Здесь можно добавить логику для регистрации пользователя
            return redirect(url_for('home'))  # Перенаправление после успешной регистрации
        else:
            # Обработка ситуации, когда одно из полей пустое
            return "Все поля обязательны для заполнения", 400
    return render_template('register.html')


@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('users'))

    return render_template('edit_user.html', user=user)

@app.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('users'))

@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)

@app.route('/search_users')
def search_users():
    query = request.args.get('query')
    users = User.query.filter(User.username.contains(query)).all()
    return render_template('users.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            return redirect(url_for('home'))
    return render_template('login.html')
