from django.db import models
from django.conf import settings
import joblib  #es una libreria que se usa para cargar el modelo
import pandas as pd
from django.contrib.auth.hashers import make_password, check_password


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
    Nombre = models.CharField(max_length=255)
    Edad = models.IntegerField()
    Genero = models.CharField(max_length=1, choices=[
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ])
    Dedos_amarillos = models.IntegerField()
    Ansiedad = models.IntegerField()
    Presión_de_pares = models.IntegerField()
    Enfermedad_crónica = models.IntegerField()
    Fatiga = models.IntegerField()
    Alergia = models.IntegerField()
    Sibilancias = models.IntegerField()
    Consumo_de_alcohol = models.IntegerField()
    Tos = models.IntegerField()
    Dificultad_para_tragar = models.IntegerField()
    Dolor_en_el_pecho = models.IntegerField()
    #ANXYELFIN = models.IntegerField()
    probability = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

