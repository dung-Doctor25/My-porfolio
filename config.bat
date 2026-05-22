@echo off

cd /d "D:\virtual environment\Porfolio"

call venv\Scripts\activate

cd Portfolio


python manage.py makemigrations
python manage.py migrate