# Generated by Django 5.1.1 on 2024-09-24 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('YELLOW_FINGERS', models.IntegerField()),
                ('ANXIETY', models.IntegerField()),
                ('PEER_PRESSURE', models.IntegerField()),
                ('CHRONIC_DISEASE', models.IntegerField()),
                ('FATIGUE', models.IntegerField()),
                ('ALLERGY', models.IntegerField()),
                ('WHEEZING', models.IntegerField()),
                ('ALCOHOL_CONSUMING', models.IntegerField()),
                ('COUGHING', models.IntegerField()),
                ('SWALLOWING_DIFFICULTY', models.IntegerField()),
                ('CHEST_PAIN', models.IntegerField()),
                ('ANXYELFIN', models.IntegerField()),
                ('probability', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
