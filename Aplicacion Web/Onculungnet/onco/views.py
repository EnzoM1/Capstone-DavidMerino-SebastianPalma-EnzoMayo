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
import json
from django.db.models import Count, Avg


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
    if request.user.username == 'skibidi':
        pacientes = PatientData.objects.all()

        # 1. Distribución por género con la probabilidad promedio de cáncer
        genero_data = pacientes.values('Genero').annotate(
            count=Count('Genero'),
            avg_probabilidad=Avg('probability')  # Promedio de probabilidad de cáncer por género
        )

        # 2. Promedio de probabilidad de cáncer por edad
        edad_data = pacientes.values('Edad').annotate(promedio_probabilidad=Avg('probability'))

        # 3. Relación entre alcohol y probabilidad
        alcohol_data = pacientes.values('Consumo_de_alcohol').annotate(promedio_probabilidad=Avg('probability'))

        # 4. Pacientes con tos y su probabilidad
        tos_probabilidad = pacientes.values('Tos').annotate(promedio_probabilidad=Avg('probability'))

        # Convertir los datos a formato JSON
        genero_data_json = json.dumps(list(genero_data))
        edad_data_json = json.dumps(list(edad_data))
        alcohol_data_json = json.dumps(list(alcohol_data))
        tos_probabilidad_json = json.dumps(list(tos_probabilidad))

        print(genero_data_json)
        print(edad_data_json)
        print(alcohol_data_json)
        print(tos_probabilidad_json)

        context = {
            'genero_data': genero_data_json,
            'edad_data': edad_data_json,
            'alcohol_data': alcohol_data_json,
            'tos_probabilidad': tos_probabilidad_json,
        }

        return render(request, 'admin/vistaAdmin.html', context)
    else:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")


def register(request):
    if request.method == 'GET':
        return render(request, 'admin/register.html', {"form": CustomUserCreationForm()})
        print("hola")
    else:
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido.')
            return redirect('index')  # Verifica que 'index' esté definido en tus URLs
        else:
            messages.error(request, 'El formulario no es válido. Por favor, corrige los errores.')
            return render(request, 'admin/register.html', {"form": form})




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
            
            # Guardar los datos del paciente en un nuevo modelo y la base de datos
            patient_data_obj = PatientData(**patient_data)
            patient_data_obj.probability = probability  # Save as a decimal (e.g., 0.85)
            patient_data_obj.save()
            
            # Convertir la probabilidad a porcentaje entero para la visualización
            probability_percentage = "{}%".format(int(round(probability * 100)))
            
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