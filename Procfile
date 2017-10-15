web: gunicorn conekta_django.wsgi
web: gunicorn conekta_django:app
web: python manage.py runserver 0.0.0.0:$PORT

[packages]
dj-database-url = "0.4.2"
django = "1.11.6"
gunicorn = "19.7.1"
conekta = "2.4.0"

[requires]
python_version = "2.7.10"
