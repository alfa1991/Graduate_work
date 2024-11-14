# Сравнение REST API на Django Rest Framework, FastAPI и Flask-RESTful

## Описание проекта
Этот проект направлен на сравнение трех различных фреймворков для разработки REST API: **Django Rest Framework**, **FastAPI** и **Flask-RESTful**. Цель проекта — продемонстрировать различия в подходах, производительности и удобстве разработки между этими инструментами.

## Структура проекта
Проект состоит из трех отдельных приложений:
- `drf_app`: приложение на **Django Rest Framework**.
- `fastapi_app`: приложение на **FastAPI**.
- `flask_app`: приложение на **Flask-RESTful**.

Каждое приложение предоставляет API для работы с данными пользователей, используя общий набор CRUD операций.

Django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
python manage.py test object_detection
python manage.py runserver   
python manage.py runserver 8080
python manage.py showmigrations


http://127.0.0.1:8080/admin/
http://127.0.0.1:8080/items/
http://127.0.0.1:8080/api/items/

Fastapi
uvicorn main:app --reload
uvicorn main:app --reload --port 8080
http://127.0.0.1:8080
wdhttp://127.0.0.1:8080/items/
http://127.0.0.1:8080/items/1
http://127.0.0.1:8080/docs
http://127.0.0.1:8080/redoc
GET /items/
GET /items/{item_id} 

flask_app
# Для инициализации базы данных
python init_db.py
# Для запуска приложения
python app.py
flask run --reload
http://127.0.0.1:5000/register
http://127.0.0.1:5000/users/
http://127.0.0.1:5000/users/1


### Файловая структура
 

# Структура проекта


Выпускная работа/
├── .venv/                       # Виртуальное окружение для изоляции зависимостей
├── db.sqlite3                   # Файл базы данных SQLite
├── manage.py                    # Скрипт для управления Django-приложением

├── drf_app/                     # Основное Django-приложение
│   ├── detection_site/          # Директория конфигурации Django-приложения
│   │   ├── __init__.py          # Указывает на то, что это пакет Python
│   │   ├── asgi.py              # Точка входа для ASGI-серверов
│   │   ├── settings.py          # Основные настройки Django
│   │   ├── urls.py              # Маршрутизация URL для приложения
│   │   └── wsgi.py              # Точка входа для WSGI-серверов
│   ├── media/                   # Директория для хранения медиафайлов
│   ├── object_detection/        # Приложение для объектного распознавания
│   │   ├── миграции/            # Файлы миграций базы данных
│   │   │   ├── 0001_initial.py  # Первая миграция
│   │   │   ├── 0002_remove_item_image_alter_item_name.py  # Вторая миграция
│   │   │   └── __init__.py
│   │   ├── шаблоны/             # Шаблоны HTML для Django-приложения
│   │   │   └── объектное распознавание/
│   │   │       ├── home.html             # Главная страница
│   │   │       └── список_элементов.html # Страница со списком элементов
│   │   ├── __init__.py
│   │   ├── admin.py             # Настройки административного интерфейса
│   │   ├── apps.py              # Конфигурация приложения
│   │   ├── models.py            # Определение моделей данных
│   │   ├── serializers.py       # Сериализация и десериализация данных
│   │   ├── signals.py           # Сигналы для обработки событий
│   │   ├── tests.py             # Тесты для приложения
│   │   ├── urls.py              # Маршруты для объектного распознавания
│   │   └── views.py             # Логика представлений для обработки запросов

├── static/                      # Директория для статических файлов Django

├── fastapi_app/                 # Приложение на FastAPI
│   ├── main.py                  # Основной файл для запуска приложения FastAPI
│   ├── models.py                # Модели данных FastAPI
│   └── views.py                 # Обработчики маршрутов FastAPI

├── flask_app/                   # Приложение на Flask
│   ├── app.py                   # Основной файл для запуска приложения Flask
│   ├── models.py                # Модели данных для Flask
│   ├── views.py                 # Обработчики маршрутов Flask
│   └── templates/               # Шаблоны HTML для Flask
│       ├── index.html           # Главная страница
│       ├── register.html        # Страница регистрации
│       └── users.html           # Страница пользователей

└── media/                       # Директория для хранения медиафайлов
    └── images/                  # Директория для хранения изображений



## Установка и запуск

### Шаг 1: Клонировать репозиторий
```bash
git clone https://github.com/yourusername/rest-api-comparison.git
cd rest-api-comparison

### Шаг 2: Установка зависимостей
Перед установкой зависимостей убедитесь, что у вас установлен Python 3.11+ и виртуальное окружение.

1. Установка зависимостей для всех фреймворков:

```bash```

pip install -r requirements.txt

2. Запуск приложений:
Фреймворк Django Rest:

bash

cd drf_app
python manage.py migrate
python manage.py runserver
FastAPI:

```bash```

cd fastapi_app
uvicorn main:app --reload
Flask-Успокаивающий:

```bash```


cd flask_app
python app.py

Шаг 3: Доступ к API
Джанго: http://127.0.0.1:8000/
FastAPI: http://127.0.0.1:8000/docs (Swagger документация)
Колба: http://127.0.0.1:5000/
Тестирование
Каждое приложение поддерживает стандартные CRUD операции для работы с пользователями.

Примеры запросов:
Получение всех пользователей (GET):
Джанго: http://127.0.0.1:8000/api/users/
FastAPI: http://127.0.0.1:8000/users/
Колба: http://127.0.0.1:5000/users/
Добавление нового пользователя (POST):
json


{
  "username": "new_user",
  "age": 25
}
Сравнение
После выполнения тестов вы можете сравнить следующие параметры:

Скорость обработки запросов.
Простота написания кода.
Документация и поддержка фреймворка.

Заключение
Проект демонстрирует, что Django Rest Framework предлагает встроенные функции, FastAPI выигрывает в производительности, а Flask-RESTful обеспечивает гибкость и простоту, но требует больше кода для реализации базовых функций.```
