# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\flask_app\app.py


from flask import Flask, render_template
from config import Config
from database import db  # Импортируйте db из database.py

app = Flask(__name__)
app.config.from_object(Config)  # Загружаем конфигурацию
db.init_app(app)  # Инициализируем db с привязкой к app

@app.route('/')
def home():
    return render_template('index.html')

# Импортируем маршруты после определения приложения
from views import *

if __name__ == '__main__':
    app.run(debug=True)



# Для запуска:python app.py
