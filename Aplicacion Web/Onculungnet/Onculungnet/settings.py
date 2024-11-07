"""
Django settings for Onculungnet project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import dj_database_url
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Establece la clave secreta de Django a partir de la variable de entorno 'SECRET_KEY'.
# Si la variable no está definida, se usará un valor por defecto (que no debe ser usado en producción).
# En entornos de producción, asegúrate de establecer 'SECRET_KEY' como una variable de entorno segura
# para proteger la aplicación de ataques y garantizar su correcto funcionamiento.

SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
# Determina el modo DEBUG basado en si la aplicación se está ejecutando en Render.
# Si la variable de entorno 'RENDER' no está presente, significa que estamos en un entorno de desarrollo,
# por lo tanto, DEBUG estará activado (True). En caso contrario, DEBUG estará desactivado (False) en producción.
# Advertencia: DEBUG debe estar en False en producción para evitar la exposición de información sensible.

DEBUG = 'RENDER' not in os.environ  

# Configura los hosts permitidos (ALLOWED_HOSTS) en Django.
# En un entorno de desarrollo, ALLOWED_HOSTS puede estar vacío.
# En producción (como en Render), Django obtiene el nombre de host externo
# a través de la variable de entorno RENDER_EXTERNAL_HOSTNAME, permitiendo el acceso al dominio correcto.
# Esta configuración es crucial para prevenir accesos no autorizados a la aplicación.

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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

# Define el punto de entrada WSGI para el proyecto Django.
# El archivo 'wsgi.py' en el directorio del proyecto Onculungnet expone la aplicación WSGI,
# que permite a Django comunicarse con servidores web como Gunicorn o uWSGI.
# Este es un paso esencial para el despliegue en producción.

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

# Database documentation https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Configura la conexión a la base de datos MySQL para el proyecto Django.
# Utiliza dj_database_url.config para cargar las credenciales desde la cadena de conexión
# y establece un tiempo máximo de reutilización de la conexión de 600 segundos (conn_max_age=600).
# Si no se proporcionan variables de entorno para la base de datos, se utiliza la configuración predeterminada.
# En este caso: mysql://root:1234@localhost:3306/Onco2

#DATABASES = {
#    'default': dj_database_url.config(
#        default='mysql://root:1234@localhost:3306/Onco2',
#        conn_max_age=600
#    )
#}

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get(
            'DATABASE_URL', 'mysql://root:1234@localhost:3306/Onco2'
        ),
        conn_max_age=600,
        ssl_require=False
    )
}

# default= 'MySQL://USER:PASSWORD@HOST:PORT/NAME',
#'ENGINE': 'django.db.backends.mysql',
#'NAME': 'Onco2',  # Nombre de la base de datos, depende de el que creó la base de datos. 
#'USER': 'root',  # O el usuario que hayas creado.
#'PASSWORD': '1234', # Contraseña que establecí cuando instalas MySQL. tu contraseña deivi "310303"
#'HOST': 'localhost', # Host local, se puede cambiar una vez tengamos el servidor.
#'PORT': '3306', # Puerto predeterminado para MySQL.


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    #{
     #   'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        
    #},
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

# Configuración para el manejo de archivos estáticos en Django.
# En producción (cuando DEBUG es False), los archivos estáticos se copian al directorio 'staticfiles'.
# Además, se utiliza WhiteNoise para comprimir los archivos estáticos y renombrarlos de manera única
# para permitir el cacheo a largo plazo en los navegadores.
# Comando utilizado para recopilar archivos estáticos: python manage.py collectstatic

STATIC_URL = 'static/'

if not DEBUG:    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_URL = 'inicioSesion' #es donde te redirige si no te has logeado

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuración del correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'oncolungnet@gmail.com'
EMAIL_HOST_PASSWORD = 'udei xccr diro ptfd'
DEFAULT_FROM_EMAIL = 'oncolungnet@gmail.com'

#clave aplicacion
#udei xccr diro ptfd
