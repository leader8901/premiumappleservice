# PREMIUM APPLE SERVICE

# Как запустить
Краткое руководство: Pooling & SQLite
Самый быстрый способ запустить бота — запустить его в режиме пула с

cd djangoProject
Создание virtual environment (опционально)

python3 -m venv (project)
source project/bin/activate
Install all requirements:

pip install -r requirements.txt
Создайте файл .env в корневом каталоге и скопируйте и вставьте это:


TELEGRAM_TOKEN=<ENTER YOUR TELEGRAM TOKEN HERE>
Run migrations to setup SQLite database:

python manage.py migrate
Create superuser to get access to admin panel:

python manage.py createsuperuser
Запускаем бота в режиме пула:

python run_pooling.py 
Если вы хотите открыть панель администратора Django, которая будет находиться по адресу http://localhost:8000/tgadmin/:
python manage.py runserver


