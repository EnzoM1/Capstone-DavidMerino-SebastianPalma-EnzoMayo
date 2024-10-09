from django import forms
from .models import PatientData
from django.core.validators import MinValueValidator, MaxValueValidator

#esto basicamente trae el modelo de models luego se crea una clase llamada patienform que vendria a ser el formulario

#hay que modificar en un futuro quiza como toma los datos para que no pongan un 2 en vez de 0 y 1

#posdata estos datos tienen que ser los mismo con los que trabajo el modelo  en colab excepto por name,age y gender

#no me acuerdo como se editaban los formularios pero se puede pa que queden mas skibidis

YES_NO_CHOICES = (
    (None, '---'),
    (1, 'Sí'),
    (0, 'No')
)

class PatientForm(forms.Form):
    Nombre = forms.CharField(label='Nombre')
    Edad = forms.IntegerField(label='Edad')
    Genero = forms.ChoiceField(label='Genero', choices=[
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ])
   

    Dedos_amarillos = forms.ChoiceField(
    label='Dedos Amarillos',
    choices=YES_NO_CHOICES,
    initial=None
    )
    Ansiedad = forms.ChoiceField(
        label='Ansiedad',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Presión_de_pares = forms.ChoiceField(
        label='Presion de pares',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Enfermedad_crónica = forms.ChoiceField(
        label='Enfermedad crónica',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Fatiga = forms.ChoiceField(
        label='Fatiga',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Alergia = forms.ChoiceField(
        label='Alergia',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Sibilancias = forms.ChoiceField(
        label='Sibilancias',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Consumo_de_alcohol = forms.ChoiceField(
        label='Consumo de alcohol',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Tos = forms.ChoiceField(
        label='Tos',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Dificultad_para_tragar = forms.ChoiceField(
        label='Dificultad para tragar',
        choices=YES_NO_CHOICES,
        initial=None
    )
    Dolor_en_el_pecho = forms.ChoiceField(
        label='Dolor en el pecho',
        choices=YES_NO_CHOICES,
        initial=None
    )