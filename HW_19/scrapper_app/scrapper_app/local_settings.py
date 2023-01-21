from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9ti+gvq$m2qt8g!$kbue*cxy#p)f(rx$vlob!f++!4277omg7!'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

