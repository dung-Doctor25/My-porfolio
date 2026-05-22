@echo off

cd /d "D:\virtual environment\Porfolio"

call venv\Scripts\activate

cd Portfolio

:loop
cls
echo =========================
echo Django Server Starting...
echo Press Ctrl + C to stop
echo =========================

python manage.py runserver

echo.
echo Server stopped or crashed.
pause

goto loop