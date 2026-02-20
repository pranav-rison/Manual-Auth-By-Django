# Manual Auth Django App

A simple Django authentication project built without Django's built-in auth system. This project demonstrates manual registration and login with basic HTML templates.

## Setup

```bash
python -m venv authenv
authenv\Scripts\activate
pip install Django
```

## Create Project and App

```bash
django-admin startproject manualauth
cd manualauth
python manage.py startapp main
```

## Run Server

```bash
python manage.py runserver
```

This creates the `db.sqlite3` file automatically.

## Register App

Add the app in `INSTALLED_APPS` in `manualauth/settings.py`:

```python
' main '
```

## Templates and Views

Create templates in `main/templates` and views in `main/views.py`:

- `home()` renders `home.html`
- `login()` renders `login.html`
- `register()` renders `register.html`
- `logout()` renders `logout.html`

## URL Configuration Options

### App-level URLs

```python
# main/urls.py
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
]

# manualauth/urls.py
path('', include('main.urls')),
```

**Best for:** multiple apps and larger projects

### Project-level URLs

```python
# manualauth/urls.py
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
]
```

**Best for:** single app or learning projects

## Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

Admin login URL:

```
http://127.0.0.1:8000/admin/login/?next=/admin/
```

## Register Page URL

```
http://127.0.0.1:8000/register/
```

## Notes

- Do not import `urllib.request` in `views.py`.
- Use `.models` for local models: `from .models import User, Login`.
- Use `POST` in `register()` to save data.

### Password Hashing (Optional)

```python
from django.contrib.auth.hashers import make_password

hash_password = make_password(password)
User.objects.create(username=username, email=email, password=hash_password, conform_password=confirm_password)
```
