Cors is to restrict and invite only certain origins.

### Get into your shell

### Pip install
```python
pipenv install django-cors-headers
```

##### This install is going to bring in the headers needed for your deployment

### Jump into your settings.py and under your installed apps, you need to add another 3rd party app:
```python
'corsheaders',
```

### Now under MIDDLEWARE you need to add the following at the very top of all of the others:
```python
'corsheaders.middleware.CorsMiddleware',
```

### Then below REST_FRAMEWORK, outside of it you need to type:
```python
CORS_ORIGIN_WHITELIST = [
    "HTTP://LOCALHOST:3000",
]
```

### Then you need to run from inside the container.
```python
docker-compose up --build
```

##### You wont be able to access local host 3000 you will get a 401 error. You are atilla able to access local host 8000. If you go in to Postman and refresh your token (not necessary right now.)


### Now setting up anvironmental variables.
##### Good websit for this is djangostars.com/blog/configuring-django-settings-best-practices/ and django-environ.readthedocs.io/en/latest/


### Now you need to install:
```python
pipenv install django-environ
```

### You need to otuch a .env file to your project folder now, so:
```python
touch manufacturer_project/.env
```

### At the top of settings under import os you want to import environ and also are going to right under that type out:
```python
env = environ.Env(
    #set casting and default value
    DEBUG=(bool, False)
)

environ.Env.read_env()
```

### Delete your SECRET_KEY in settings and make it equal to env.stR('SECRET_KEY')

### Now delete what DEBUG is currently equal to and make it equal to env.bool('DEBUG')

### Now you want to make sure your DATABASES look like this:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER':env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    }
}
```

### Now go into your ALLOWED_HOSTS and make it look like:
```python
ALLOWED_HOSTS =tuple(env.list('ALLOWED_HOSTS'))
```
###
###
###
###
###
###
###