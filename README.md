# Letscycle
An app for cycling and having fun :)

## Setting up - Backend
This app was made with Django (3.2), using PostgreSQL as DB.

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

6. Run the Backend Server
```bash
python letscycle/manage.py runserver
```

## Setting up - Frontend
The frontend of this app was made with React.
To run the frontend application, go to the `ui/` folder.

1. Setup package.json
On the beginning of the file `ui/package.json`, set the parameter **proxy**, pointing to the host and port that you're runnning the backend

2. Install the depencies
```bash
yarn install
```

3. Run the frontend application
```bash
yarn start
```
