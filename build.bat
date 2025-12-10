@echo off
pip install -r requirements.txt
python manage.py collectstatic --noinput --clear
python manage.py migratepython