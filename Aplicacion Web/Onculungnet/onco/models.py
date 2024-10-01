from django.db import models
from django.conf import settings
import joblib  #es una libreria que se usa para cargar el modelo
import pandas as pd


#los demas imports quizan no sean necesarios se pueden eliminar en un futuro para tener un codigo mas clean

# Cargar el modelo desde el archivo
lr_model = joblib.load('onco/modelos/lr_model.pkl')


# Creamos la clase PatientData que nos sirve para guardar los datos del formulario.
# name = nombre.
# age = edad.
# gender = genero.
# yellow fingers = dedos amarillos .
# anxiety = ansiedad .
# allergy = alergias.
# wheezing = sibilancias, son los sonidos silbantes o chillones al respirar.
# alcohol consuming = consumo de alcohol.
# coughing = toser.
# swallowing difficulty = dificultad para tragar.
# chest pain = dolor de pecho.
# anxyelfin = no recuerdo que era pero no importa ya que para el analisis no es importante y lo eliminaremos en un futuro.
# probability = probabilidad, este campo guarda el resultado final de la encuesta y se muestra en forma de porcentaje.
# created at = fecha de cracion, este campo guarda la fecha en la que se rellena el formulario.

class PatientData(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    YELLOW_FINGERS = models.IntegerField()
    ANXIETY = models.IntegerField()
    PEER_PRESSURE = models.IntegerField()
    CHRONIC_DISEASE = models.IntegerField()
    FATIGUE = models.IntegerField()
    ALLERGY = models.IntegerField()
    WHEEZING = models.IntegerField()
    ALCOHOL_CONSUMING = models.IntegerField()
    COUGHING = models.IntegerField()
    SWALLOWING_DIFFICULTY = models.IntegerField()
    CHEST_PAIN = models.IntegerField()
    ANXYELFIN = models.IntegerField()
    probability = models.CharField(null=True, blank=True,max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class user(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)