from django import forms
from .models import PatientData

#esto basicamente trae el modelo de models luego se crea una clase llamada patienform que vendria a ser el formulario

#hay que modificar en un futuro quiza como toma los datos para que no pongan un 2 en vez de 0 y 1

#posdata estos datos tienen que ser los mismo con los que trabajo el modelo  en colab excepto por name,age y gender

#no me acuerdo como se editaban los formularios pero se puede pa que queden mas skibidis

class PatientForm(forms.Form):
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    YELLOW_FINGERS = forms.IntegerField(label='Yellow Fingers (1 for YES, 0 for NO)')
    ANXIETY = forms.IntegerField(label='Anxiety (1 for YES, 0 for NO)')
    PEER_PRESSURE = forms.IntegerField(label='Peer Pressure (1 for YES, 0 for NO)')
    CHRONIC_DISEASE = forms.IntegerField(label='Chronic Disease (1 for YES, 0 for NO)')
    FATIGUE = forms.IntegerField(label='Fatigue (1 for YES, 0 for NO)')
    ALLERGY = forms.IntegerField(label='Allergy (1 for YES, 0 for NO)')
    WHEEZING = forms.IntegerField(label='Wheezing (1 for YES, 0 for NO)')
    ALCOHOL_CONSUMING = forms.IntegerField(label='Alcohol Consuming (1 for YES, 0 for NO)')
    COUGHING = forms.IntegerField(label='Coughing (1 for YES, 0 for NO)')
    SWALLOWING_DIFFICULTY = forms.IntegerField(label='Swallowing Difficulty (1 for YES, 0 for NO)')
    CHEST_PAIN = forms.IntegerField(label='Chest Pain (1 for YES, 0 for NO)')
    ANXYELFIN = forms.IntegerField(label='AAnxieelfuin (1 for YES, 0 for NO)')