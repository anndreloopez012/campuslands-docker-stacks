import os
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "campus_local_secret")
DEBUG = True
ALLOWED_HOSTS = ["*"]
ROOT_URLCONF = "campus.urls"
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth"]
DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql", "HOST": "postgres", "NAME": os.getenv("POSTGRES_DB"), "USER": os.getenv("POSTGRES_USER"), "PASSWORD": os.getenv("POSTGRES_PASSWORD"), "PORT": "5432"}}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
USE_TZ = True
