from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseForbidden
from .models import lr_model, PatientData
from django.contrib.auth.models import User #es un modelo de usuario que no fue necesario crear porque ya lo tenia
from django.contrib.auth import login, logout, authenticate #temas de autenticacion
from .forms import PatientForm,CustomUserCreationForm 
from django.contrib import messages #esto tira los mensajes
import pandas as pd
from django.contrib.auth.forms import UserCreationForm #este es un form que trae el django para guardar los users
from django.db import IntegrityError #simplemente un mensaje de error
from django.contrib.auth.decorators import login_required #esto protege las urls
import csv


#imports necesarios para que funcione la view

#ahora se llama login pa no confundir la vista

#de momento el register se puede entrar sin necesidad de iniciar, tienen que crear el usuario "skibidi" la contra la que sea y iniciado con el skibidi en la url ponen /vistaAdmin

#si entran con otro usuario osea crean otro cualquiera y intentan ingresar a /vistaAdmin no van a tener acceso




def pagina_inicio(request):
    return render(request, 'test_index.html')

def sintomas(request):
    return render(request, 'sintomas.html')


@login_required
def vistaAdmin(request):
     # Verifica si el usuario es el correcto
    if request.user.username == 'skibidi':  # Reemplaza con el nombre de usuario específico
        return render(request, 'admin/vistaAdmin.html')  # Reemplaza con tu template
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")


def register(request):
    if request.method == 'GET':
        return render(request, 'admin/register.html', {"form": CustomUserCreationForm()})
    else:
        # Crear una instancia del formulario con los datos POST
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'El formulario no es válido. Por favor, corrige los errores.')
            # Si el formulario no es válido, devuelve el formulario con errores
            return render(request, 'admin/register.html', {"form": form, "error": "Formulario inválido."})




def inicio(request):
     
     if request.method == 'POST':
        # Recoge el nombre de usuario y la contraseña del formulario
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autentica al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Si la autenticación es exitosa, inicia sesión
            login(request, user)
             # Verifica si el usuario es el específico
            if user.username == 'skibidi':  # <----- es el admin
                return redirect('vistaAdmin')  # Redirige a la vista especial
            else:
                return redirect('form')  # Redirige a la página del formulario
            
            

        else:
            # Si las credenciales no son correctas, muestra un error
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    
     return render(request, 'index.html')  # Asegúrate de que esta sea tu plantilla de inicio de sesión

@login_required
def predict_probability(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_data = form.cleaned_data
            # Crear un dataframe con los datos del paciente
            patient_df = pd.DataFrame([patient_data])
            
            # Seleccionar las características correctas
            selected_features = patient_df[['Dedos_amarillos', 'Ansiedad', 'Presión_de_pares', 'Enfermedad_crónica', 
                                            'Fatiga', 'Alergia', 'Sibilancias', 'Consumo_de_alcohol', 
                                            'Tos', 'Dificultad_para_tragar', 'Dolor_en_el_pecho']]
            
            # Ajustar los nombres de las columnas para que coincidan con los del modelo entrenado
            selected_features.columns = selected_features.columns.str.replace(' ', '_')  # Reemplaza espacios por guiones bajos

            # Predecir la probabilidad de cáncer
            probability = lr_model.predict_proba(selected_features)[:, 1][0]
            
            # Convertir la probabilidad a porcentaje entero
            probability_percentage = "{}%".format(int(round(probability * 100)))
            
            # Guardar los datos del paciente en un nuevo modelo y la base de datos
            patient_data_obj = PatientData(**patient_data)
            patient_data_obj.probability = probability_percentage
            patient_data_obj.save()
            
            return render(request, 'result.html', {'probability': probability_percentage})
    else:
        form = PatientForm()
    return render(request, 'form.html', {'form': form})


def listar_pacientes(request):
    # Obtener todos los datos de la tabla
    patients = PatientData.objects.all()  
    return render(request, 'admin/listar_pacientes.html', {'patients': patients})

def descargar_csv(request):
    # Crear una respuesta de tipo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pacientes.csv"'

    # Crear el escritor CSV
    writer = csv.writer(response)

    # Escribir el encabezado
    writer.writerow([
        'Nombre', 'Edad', 'Género', 'Dedos Amarillos', 'Ansiedad', 'Presión de Pares',
        'Enfermedad Crónica', 'Fatiga', 'Alergia', 'Sibilancias', 'Consumo de Alcohol',
        'Tos', 'Dificultad para Tragar', 'Dolor en el Pecho', 'Probabilidad de Cáncer'
    ])

    # Obtener los datos de los pacientes
    patients = PatientData.objects.all().values_list(
        'Nombre', 'Edad', 'Genero', 'Dedos_amarillos', 'Ansiedad', 'Presión_de_pares', 
        'Enfermedad_crónica', 'Fatiga', 'Alergia', 'Sibilancias', 'Consumo_de_alcohol', 
        'Tos', 'Dificultad_para_tragar', 'Dolor_en_el_pecho', 'probability'
    )

    # Escribir los datos de los pacientes
    for patient in patients:
        writer.writerow(patient)

    return response



def PasswordResetView(request):
    return render(request, 'PasswordResetView.html')

def PasswordResetConfirmView(request):
    return render(request, 'PasswordResetConfirmView.html')

@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('pagina_inicio')