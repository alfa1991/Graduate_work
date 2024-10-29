# C:\Users\Ilgiz Agliullin\PycharmProjects\Graduate_work\drf_app\detection_site\settings.py

import os  # Импортируем модуль os для работы с файловой системой
from pathlib import Path  # Импортируем класс Path для работы с путями
from decouple import config  # Импортируем функцию config для работы с переменными окружения

# Путь к корневому каталогу проекта
BASE_DIR = Path(__file__).resolve().parent.parent  # Определяем корневую директорию проекта

# Безопасный ключ для Django
SECRET_KEY = config('SECRET_KEY', default='your-secret-key')  # Получаем секретный ключ из переменных окружения

# Режим отладки
DEBUG = config('DEBUG', default=True, cast=bool)  # Получаем режим отладки из переменных окружения

# Разрешенные хосты
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Указываем разрешенные хосты для приложения

# Приложения проекта
INSTALLED_APPS = [
    'django.contrib.admin',  # Приложение административной панели
    'django.contrib.auth',  # Приложение аутентификации
    'django.contrib.contenttypes',  # Приложение для работы с типами контента
    'django.contrib.sessions',  # Приложение для работы с сессиями
    'django.contrib.messages',  # Приложение для работы с сообщениями
    'django.contrib.staticfiles',  # Приложение для работы со статическими файлами
    'rest_framework',  # Приложение Django REST Framework для создания API
    'object_detection',  # Ваше приложение для обнаружения объектов
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Middleware для обработки CORS
    'django.middleware.security.SecurityMiddleware',  # Middleware для безопасности
    'django.contrib.sessions.middleware.SessionMiddleware',  # Middleware для работы с сессиями
    'django.middleware.common.CommonMiddleware',  # Общие middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # Middleware для защиты от CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Middleware для аутентификации
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware для работы с сообщениями
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Middleware для защиты от Clickjacking
]

# Корневые URL
ROOT_URLCONF = 'detection_site.urls'  # Указываем файл с корневыми URL

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Указываем бэкенд шаблонов
        'DIRS': [BASE_DIR / 'templates'],  # Указываем директорию для пользовательских шаблонов
        'APP_DIRS': True,  # Включаем поиск шаблонов в приложениях
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Процессор контекста для отладки
                'django.template.context_processors.request',  # Процессор контекста для запросов
                'django.contrib.auth.context_processors.auth',  # Процессор контекста для аутентификации
                'django.contrib.messages.context_processors.messages',  # Процессор контекста для сообщений
            ],
        },
    },
]

# WSGI-приложение
WSGI_APPLICATION = 'detection_site.wsgi.application'  # Указываем WSGI-приложение

# Настройка базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Указываем движок базы данных
        'NAME': BASE_DIR / 'db.sqlite3',  # Указываем имя базы данных
    }
}

# Пароли
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Проверка на схожесть атрибутов пользователя
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Проверка на минимальную длину пароля
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Проверка на распространенные пароли
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Проверка на числовые пароли
    },
]

LOGGING = {
    'version': 1,  # Версия конфигурации логирования
    'disable_existing_loggers': False,  # Не отключаем существующие логгеры
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',  # Обработчик для вывода в консоль
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],  # Используем консольный обработчик
            'level': 'INFO',  # Уровень логирования
        },
    },
}

# Локализация
LANGUAGE_CODE = 'en-us'  # Код языка
TIME_ZONE = 'UTC'  # Часовой пояс
USE_I18N = True  # Использование интернационализации
USE_L10N = True  # Использование локализации
USE_TZ = True  # Использование временных зон

# Статические файлы
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Указываем директорию для статических файлов
STATIC_URL = '/static/'  # URL для доступа к статическим файлам

# Медиа-файлы (для загрузки изображений)
MEDIA_URL = '/media/'  # URL для доступа к медиафайлам
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Директория для хранения медиафайлов

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Укажите разрешенные источники для CORS
]
