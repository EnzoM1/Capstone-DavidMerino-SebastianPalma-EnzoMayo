# Generated by Django 5.1 on 2024-10-07 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onco', '0004_rename_password_usuario_contra_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
