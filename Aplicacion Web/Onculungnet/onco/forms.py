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
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    gender = forms.ChoiceField(label='Gender', choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ])
    #YELLOW_FINGERS = forms.IntegerField(label='Yellow Fingers (1 for YES, 0 for NO)')
    #ANXIETY = forms.IntegerField(label='Anxiety (1 for YES, 0 for NO)')
    #PEER_PRESSURE = forms.IntegerField(label='Peer Pressure (1 for YES, 0 for NO)')
    #CHRONIC_DISEASE = forms.IntegerField(label='Chronic Disease (1 for YES, 0 for NO)')
    #FATIGUE = forms.IntegerField(label='Fatigue (1 for YES, 0 for NO)')
    #ALLERGY = forms.IntegerField(label='Allergy (1 for YES, 0 for NO)')
    #WHEEZING = forms.IntegerField(label='Wheezing (1 for YES, 0 for NO)')
    #ALCOHOL_CONSUMING = forms.IntegerField(label='Alcohol Consuming (1 for YES, 0 for NO)')
    #COUGHING = forms.IntegerField(label='Coughing (1 for YES, 0 for NO)')
    #SWALLOWING_DIFFICULTY = forms.IntegerField(label='Swallowing Difficulty (1 for YES, 0 for NO)')
    #CHEST_PAIN = forms.IntegerField(label='Chest Pain (1 for YES, 0 for NO)')
    #ANXYELFIN = forms.IntegerField(label='AAnxieelfuin (1 for YES, 0 for NO)')

    #esos son opciones de si y no lo de arriba es como estaba antes

    YELLOW_FINGERS = forms.ChoiceField(
    label='Yellow Fingers',
    choices=YES_NO_CHOICES,
    initial=None
    )
    ANXIETY = forms.ChoiceField(
        label='Anxiety',
        choices=YES_NO_CHOICES,
        initial=None
    )
    PEER_PRESSURE = forms.ChoiceField(
        label='Peer Pressure',
        choices=YES_NO_CHOICES,
        initial=None
    )
    CHRONIC_DISEASE = forms.ChoiceField(
        label='Chronic Disease',
        choices=YES_NO_CHOICES,
        initial=None
    )
    FATIGUE = forms.ChoiceField(
        label='Fatigue',
        choices=YES_NO_CHOICES,
        initial=None
    )
    ALLERGY = forms.ChoiceField(
        label='Allergy',
        choices=YES_NO_CHOICES,
        initial=None
    )
    WHEEZING = forms.ChoiceField(
        label='Wheezing',
        choices=YES_NO_CHOICES,
        initial=None
    )
    ALCOHOL_CONSUMING = forms.ChoiceField(
        label='Alcohol Consuming',
        choices=YES_NO_CHOICES,
        initial=None
    )
    COUGHING = forms.ChoiceField(
        label='Coughing',
        choices=YES_NO_CHOICES,
        initial=None
    )
    SWALLOWING_DIFFICULTY = forms.ChoiceField(
        label='Swallowing Difficulty',
        choices=YES_NO_CHOICES,
        initial=None
    )
    CHEST_PAIN = forms.ChoiceField(
        label='Chest Pain',
        choices=YES_NO_CHOICES,
        initial=None
    )
    ANXYELFIN = forms.ChoiceField(
        label='AAnxieelfuin',
        choices=YES_NO_CHOICES,
        initial=None
    )