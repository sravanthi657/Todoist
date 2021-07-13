## Todos

### Requirements:
* Python Environment: python3 -m venv <environment_name>
* Django installation : pip3 install django
* POSTGRES : https://phoenixnap.com/kb/how-to-install-postgresql-on-ubuntu
* psycog adapter :  pip install django psycopg2


> Run: python manage.py runserver

I've worked with POSTGRES through terminal which is recommended to learn commmands and alternatively can use pgadmin.

- <u>postgres integration:</u>
> DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tododb',
        'USER': 'stella',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'POST': '',
    }
}

created using the follwing commands:
In psql prompt:
* User Creation 
> CREATE DATABASE tododb;
CREATE USER stella WITH PASSWORD ‘1234‘;
ALTER ROLE stella SET client_encoding TO ‘utf8’;
ALTER ROLE stella SET default_transaction_isolation TO ‘read committed’;
ALTER ROLE stella SET timezone TO ‘UTC’;
GRANT ALL PRIVILEGES ON DATABASE tododb TO stella;




[source code] (https://github.com/sravanthi657/Todoist)
