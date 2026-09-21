  # Django Blog Site

Учебный проект блога на Django. Пользователи могут регистрироваться, публиковать
посты с изображениями, ставить лайки, а также искать и фильтровать посты по
автору, категории и тегам.

## Функциональность

- Кастомная модель пользователя (`CustomUser`): телефон, город, аватар
- Создание, редактирование и удаление постов (только автором поста)
- Загрузка до трёх изображений к посту
- Лайки постов
- Категории и теги для постов
- Поиск по заголовку и тексту постов
- Фильтрация по автору, категории и тегу
- Сортировка по дате, заголовку и количеству лайков
- Страница «Мои посты» и страница постов конкретного автора
- Оптимизация запросов к БД: `select_related`, `prefetch_related`, `annotate`

## Технологии

- Python 3
- Django 5.1
- SQLite (по умолчанию) / PostgreSQL (опционально)
- Pillow (работа с изображениями)
- python-dotenv (переменные окружения)

## Структура проекта
├── blog/ # приложение блога: модели, формы, представления
├── users/ # приложение пользователей: кастомная модель User
├── config/ # настройки проекта (settings, urls, wsgi)
├── templates/ # HTML-шаблоны
├── static/ # статические файлы (CSS, JS)
├── media/ # загруженные файлы (изображения постов, аватары)
├── manage.py
└── requirements.txt


## Установка и запуск

1. Клонируйте репозиторий:

  ```bash
   git clone https://github.com/vladimirperov85/django_block_site.git
   cd django_block_site
   ```

2. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Примените миграции:

   ```bash
   python manage.py migrate
   ```

5. Создайте суперпользователя (для доступа к админке):

   ```bash
   python manage.py createsuperuser
   ```

6. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

7. Откройте в браузере: http://127.0.0.1:800/

## Переключение на PostgreSQL (опционально)

По умолчанию проект использует SQLite. Для работы с PostgreSQL:

1. Раскомментируйте блок настроек PostgreSQL в `config/settings.py`
2. Создайте файл `.env` в корне проекта с перемеными:

  ```
   DB_NAME=имя_базы
   DB_USER=пользователь
   DB_PASSWORD=пароль
   DB_HOST=localhost
   DB_PORT=5432
   ``

## Что изучалось в проекте

- Кастомная модель пользователя (`AUTH_USER_MODEL`)
- Связи моделей: `ForeignKey`, `ManyToManyField`
- Оптимизация ORM-запросов (`select_related`, `prefetch_related`, `annotate`)
- Фильтрация и поиск (`Q`-объекты, `icontains`)
- Загрузка файлов изображений (`ImageField`, `request.FILES`)
- Контроль доступа (`@login_required`, проверка автора поста)
- Собщения фреймворка (`django.contrib.messages`)
