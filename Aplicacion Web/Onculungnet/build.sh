#!/usr/bin/env bash
# Exit on error
set -o errexit

## Este archivo .sh se ejecuta cuando se inicia el servidor en Render

# Instala todas las dependencias del proyecto desde el archivo requirements.txt.
# Esto asegura que se utilicen las versiones adecuadas de las librerías necesarias
# para el correcto funcionamiento del proyecto.
pip install -r requirements.txt

# Recopila todos los archivos estáticos de las aplicaciones del proyecto Django en el directorio STATIC_ROOT.
# El flag --no-input evita la interacción del usuario, lo que es útil para despliegues automatizados.
python manage.py collectstatic --no-input

# Aplica las migraciones de base de datos, sincronizando la estructura de la base de datos
# con los cambios realizados en los modelos de la aplicación.
python manage.py makemigrations

python manage.py migrate && python create_superuser.py
