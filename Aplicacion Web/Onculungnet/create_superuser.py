import os
import django
from django.contrib.auth import get_user_model
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Onculungnet.settings')
django.setup()

User = get_user_model()

# Superusuario por defecto
SUPERUSER_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME', 'oncoAdmin')
SUPERUSER_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL', 'en.mayo@duocuc.cl')
SUPERUSER_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin')

if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    User.objects.create_superuser(
        username=SUPERUSER_USERNAME,
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD
    )
    print(f"Superuser '{SUPERUSER_USERNAME}' created successfully.")
else:
    print(f"Superuser '{SUPERUSER_USERNAME}' already exists.")

