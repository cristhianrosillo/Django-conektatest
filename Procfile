web: gunicorn conekta_django.wsgi
web: gunicorn conekta_django:app
web: python manage.py runserver
web: python django manage.py runserver
python manage.py runserver 0.0.0.0:8000 --noreload

[packages]
dj-database-url = "0.4.2"
django = "1.11.6"
gunicorn = "19.7.1"
conekta = "2.4.0"

[requires]
python_version = "2.7.10"
