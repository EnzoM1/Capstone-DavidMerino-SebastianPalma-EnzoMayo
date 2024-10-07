"""
Django settings for Onculungnet project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v7$qaq=r297vmo0sz6_f-#a$7ax)g%gwzf+wf#@i!)i^+08+i9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'onco',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Onculungnet.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Onculungnet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Creacion de la base de datos, cambiamos de sqlite3 a MySql para poder migrarla a AWS una vez tengamos el host.
# Cosas como el name y password son cosas momentaneas que una vez en el host modificaremos.
# La base de datos por ahora se encuentra en el tipo default pero se puede dejar la default y agregar otra, no hay problema.
# Utilizamos MySQL server y MySQL Workbench para la base de datos.
# MySQL Workbench nos ayuda a visualizar cambios y hacer consultas a la base de datos.
# El Host se cambia una vez tengamos el servidor al que vamos a migrar.

## TUTORIAL INSTALACION MYSQL PASO A PASO
# Mi contraseña de la base de datos es 310303 y el nombre es Onco.
# Primero te descargas el instalador de MysSQL https://dev.mysql.com/downloads/installer/
# Elegir la que dice (mysql-installer-web-community-8.0.39.0.msi) tiene 2.1M de descargas o algo así, es el primero de los 2.
# Es una herramienta para instalar varias cosas de MySQL pero no unico que necesitas es MySQL server y el MySQL workbench.

## CREACION DE LA BASE DE DATOS PASO A PASO
# Cuando instalas MySQL te pide poner una contraseña, esa debes usar para ingresar al CMD de MySQL se llama MySQL command line client.
# si no te pide nada usa esto mysql -u root -p para ingresar.
# Si te pide contraseña normalmente con apretar enter deberia bastar.
# Luego escribir = CREATE DATABASE nombre_de_tu_base_de_datos; 
# De nombre le puse Onco.

## INSTALACIONES QUE SE DEBE TENER HECHAS PARA QUE FUNCIONE LA BASE DE DATOS
# pip install mysqlclient.

# PARA FINALIZAR 
# Usa el python manage.py makemigrations
# Usa el python manage.py migrate 
# para guardar los cambios.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Onco2',  # Nombre de la base de datos, depende de el que creó la base de datos. 
        'USER': 'root',  # O el usuario que hayas creado.
        'PASSWORD': '1234', # Contraseña que establecí cuando instalas MySQL. tu contraseña deivi "310303"
        'HOST': 'localhost', # Host local, se puede cambiar una vez tengamos el servidor.
        'PORT': '3306', # Puerto predeterminado para MySQL.
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
LOGIN_URL = 'inicio' #es donde te redirige si no te has logeado

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuración del correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '@gmail.com'  # Cambia esto por tu correo
EMAIL_HOST_PASSWORD = 'ihvsgeyqaehpapup'  # Cambia esto por tu contraseña de correo
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
