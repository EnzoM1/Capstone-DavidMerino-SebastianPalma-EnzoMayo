from django import forms
from .models import PatientData
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#esto basicamente trae el modelo de models luego se crea una clase llamada patienform que vendria a ser el formulario

#hay que modificar en un futuro quiza como toma los datos para que no pongan un 2 en vez de 0 y 1

#posdata estos datos tienen que ser los mismo con los que trabajo el modelo  en colab excepto por name,age y gender

#no me acuerdo como se editaban los formularios pero se puede pa que queden mas skibidis

from django import forms


YES_NO_CHOICES = (
    (1, 'Sí'),
    (0, 'No'),
    (None, '--')
)

GENERO_CHOICES = (
    ('H', 'Hombre'),
    ('M', 'Mujer'),
    ('O', 'Otros'),
    ('P', 'Prefiero no decirlo'),
    (None, '--')
)



class PatientForm(forms.Form):
    Nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control'}))
    Edad = forms.IntegerField(label='Edad', 
                              widget=forms.NumberInput(attrs={'class': 'form-control'}),
                              min_value= 18, # Edad minima (puede aumentar)
                              max_value=110,
                              error_messages={
                              'min_value': 'La edad no puede ser menor de 18 años.',
                              'max_value': 'La edad no puede ser mayor de 110 años.',
                            }) # Edad maxima 
    
    Genero = forms.ChoiceField(
        label='Género',
        choices=GENERO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),  # Asegúrate de que use la clase CSS correspondiente
        initial= None
    )
    
    # Usar CheckboxSelectMultiple para mostrar como checkboxes
    Dedos_amarillos = forms.ChoiceField(
        label='Dedos Amarillos',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Ansiedad = forms.ChoiceField(
        label='Ansiedad',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Presión_de_pares = forms.ChoiceField(
        label='Presión de pares',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Enfermedad_crónica = forms.ChoiceField(
        label='Enfermedad crónica',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Fatiga = forms.ChoiceField(
        label='Fatiga',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Alergia = forms.ChoiceField(
        label='Alergia',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Sibilancias = forms.ChoiceField(
        label='Sibilancias',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Consumo_de_alcohol = forms.ChoiceField(
        label='Consumo de alcohol',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Tos = forms.ChoiceField(
        label='Tos',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Dificultad_para_tragar = forms.ChoiceField(
        label='Dificultad para tragar',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )
    Dolor_en_el_pecho = forms.ChoiceField(
        label='Dolor en el pecho',
        choices=YES_NO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=None
    )




class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Ingrese una dirección de correo válida.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):

        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    # Asegurarte de que el nombre de usuario no se quede vacío
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:  # Si username está vacío
            raise forms.ValidationError('El nombre de usuario es obligatorio.')
        # Verificar si el nombre de usuario ya está en uso
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    # Asegurarte de que el correo no se quede vacío
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:  # Si el email está vacío
            raise forms.ValidationError('El correo electrónico es obligatorio.')
        # Verificar si el correo electrónico ya está en uso
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email