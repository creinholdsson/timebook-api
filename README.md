timebook-api
============

Aims to be a simple api to track time on different projects.

Uses Django, `https://www.djangoproject.com/` and Django REST Framework, `http://www.django-rest-framework.org/`. To migrate the database, South `http://south.aeracode.org/` is used.

Setup
============


1) To install dependencies 
   `pip install django`
   `pip install djangorestframework`
   `pip install south`
   
2) DB settings
   edit the database section in the file `timebook/settings.py`
   
      ```DATABASES = {
         'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'database name',
         'USER': 'user name',
         'PASSWORD': 'password',
         'HOST': 'localhost',
         'PORT': 5432
         }
      }```


3) Set up database according to model
    `./manage.py syncdb`
    
4) To run
    `./manage.py runserver`
