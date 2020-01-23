# Authorization

### First you need to install:

```python
pipenv install djangorestframework_simplejwt psycopg2-binary Django djangorestframework
```

### Jump into a shell

### In settings.py you are going to make an addition to REST_FRAMEWORK, IT SHOULD NOW LOOK LIKE:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}
```

### In project urls.py you want to to add an import and two additional paths:
```python
from rest_framework_simplejwt import views as jwt_views

path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

```

### So now you should look like this:
```python
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('vehicle.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
```

### Then in your terminal you want to use Docker to build the project.
```python
docker-compose up --build
```

### Create a superuser inside the container. (open a new terminal tab/window while running the server)
```python
docker-compose run web ./manage.py migrate

docker-compose run web ./manage.py createsuperuser
```

### Go to Postman now and create a new collection. Under the Body tab you want to select x-www-form. Add a username and password field and input your information in there.

### Next to POST you want to put http://localhost:8000/api/token/

### Now hit send and you should recieve 2 tokens "refresh" and "access"

### Save to collections (save as obtain_token)

### Now create a GET request and click the Auth tab and select the Bearer Token. Next to GET you are going to put http://localhost:8000/api/v1/ which matches the desired path.

### Input your access token and hit send. You chould recieve an empty array []. Congrats. Key should only really last 5 min. (save as get_resource)

### Create another POST using http://127.0.0.1:8000/api/token/refresh/. Under the body tab, select the x-www-form again on this one. Make refresh the key and the value is going to be your refresh token. Hit send and you now have a new access token. (save as refresh_token).

### Place that new key inside your get_resources instead and instead of getting an empty array, you should get whatever is in that database.

### Create a PUT now and use http://localhost:8000/api/v1/1/. Under Auth you are going to set another Bearer Token to that previously mentioned new token.

### Under body go to x-www-form and add the fields you are wanting to add. Save this as update_resource.

### Go back into your code under settings.py and under DEFAULT_AUTHENTICATION you should have 3 more items. So under that should look like this:  This key will last much longer.
```python
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
```

### Install Gunicorn
```python
pipenv install gunicorn
```

Missed an bunch of notes but was able to debug pretty quick using the below snippits of code.
```python
'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework_simplejwt.authentication.JWTAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.BasicAuthentication',
]
```
```python
djangorestframework-simplejwt = "*"
gunicorn = "*"
whitenoise = "*"
```

```python
from rest_framework_simplejwt import views as jwt_views
```

```python
path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
```

```python
command: gunicorn blog_project.wsgi:application --bind 0.0.0.0:8000
```

```python
'django.contrib.sessions.middleware.SessionMiddleware',
'whitenoise.middleware.WhiteNoiseMiddleware',
'django.middleware.common.CommonMiddleware',
```

```python
'django.contrib.messages',
'whitenoise.runserver_nostatic',
'django.contrib.staticfiles',
```

```python
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

```