# Letscycle
An app for cycling and having fun :)

## Setting up
This app was made with Django, using PostgreSQL as DB.

1. Create your database
```bash
psql -U postgres
```
Or use your db user and password. Then,
```
postgres=# CREATE DATABASE <db_name>;
```

2. In your Python Environment, install the dependencies:
```bash
pip install -r requirements.txt
```

3.  Edit you  `SECRET_KEY`  in your  `settings.py`
4.  Edit you  `DATABASES`  in your  `settings.py`:

``` python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': <db_name>,
		'USER': <db_name>,
		'PASSWORD': <db_password>,
		'HOST': 'localhost',
		'PORT': '5432',
	}
}
```
5. Run the migrations!
```bash
python letscycle/manage.py migrate
```

6. Now, you're good to go!
```bash
python letscycle/manage.py runserver
```