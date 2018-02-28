# LAS

LAS is a Life Alert Service where users can get medical service just a click away. 

### Steps to Setup:

1. git clone git@github.com:sainikitha99/LAS.git (OR) https://github.com/sainikitha99/LAS.git
2. Create virtual environment with the name `las`
3. Go to project folder and install requirements `pip install -r requirements.txt`
4. Set the environment variables `source .env`
5. Since we are using `PostgreSQL` database, you need to create a database with the name `las`
6. Create a role (user) called `lasuser` and alter role permissions as below
   ```
   CREATE ROLE lasuser;
   ALTER ROLE lasuser WITH LOGIN SUPERUSER CREATEROLE CREATEDB REPLICATION;
   ALTER ROLE lasuser WITH PASSWORD 'las1pass`;
   ```
7. Now grant privilieges to the new role `GRANT ALL PRIVILEGES ON DATABASE las TO lasuser;`
8. Add these settings to `local_settings.py` (This is to maintain separate settings only for localhost.)
    ```
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'las', # database_name
        'USER': 'lasuser', # database_user
        'PASSWORD': 'las1pass', # password
        'HOST': 'localhost', # host
        'PORT': '5432' # default port for postgres.
        }
    }
    ```
9. Time to migrate the tables to database `python manage.py migrate`
10. Create superuser `python manage.py createsuperuser`. This is only for admin.
11. Runserver `python manage.py runserver`