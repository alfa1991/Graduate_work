# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\app.py

from flask import Flask, render_template
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

# Импортируем маршруты после определения приложения
from views import *  # Импортируем маршруты из views.py

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


# Для запуска:python app.py
