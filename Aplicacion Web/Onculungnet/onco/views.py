from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseForbidden
from .models import lr_model, PatientData
from django.contrib.auth.models import User #es un modelo de usuario que no fue necesario crear porque ya lo tenia
from django.contrib.auth import login, logout, authenticate #temas de autenticacion
from .forms import PatientForm,CustomUserCreationForm 
from django.contrib import messages #esto tira los mensajes
import pandas as pd
from django.contrib.auth.forms import UserCreationForm #este es un form que trae el django para guardar los users
from django.db import IntegrityError #simplemente un mensaje de error
from django.contrib.auth.decorators import login_required, user_passes_test#esto protege las urls
import csv
import json
from django.db.models import Count, Avg


#imports necesarios para que funcione la view

#ahora se llama login pa no confundir la vista

#de momento el register se puede entrar sin necesidad de iniciar, tienen que crear el usuario "skibidi" la contra la que sea y iniciado con el skibidi en la url ponen /vistaAdmin

#si entran con otro usuario osea crean otro cualquiera y intentan ingresar a /vistaAdmin no van a tener acceso





#views mas ordenadas


#super user es OncoAdmin clave : admin --mejorar con algun generador




# Función de prueba que verifica si el usuario es un superusuario
def is_superuser(user):
    return user.is_superuser

# Vista de inicio de la aplicación
def pagina_inicio(request):
    return render(request, 'test_index.html')

# Vista de inicio de sesión
def inicioSesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vistaAdmin' if user.is_superuser else 'form')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    return render(request, 'inicioSesion.html')

# Vista de registro de usuarios
def register(request):
    if request.method == 'GET':
        return render(request, 'admin/register.html', {"form": CustomUserCreationForm()})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido.')
            return redirect('inicioSesion')
        else:
            messages.error(request, 'El formulario no es válido. Por favor, corrige los errores.')
            return render(request, 'admin/register.html', {"form": form})

# Vista de cierre de sesión
@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('pagina_inicio')

# Vista de síntomas (solo para usuarios autenticados)
@login_required
def sintomas(request):
    return render(request, 'sintomas.html')

# Vista para predecir la probabilidad de cáncer (solo para usuarios autenticados)
@login_required
def predict_probability(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_data = form.cleaned_data
            patient_df = pd.DataFrame([patient_data])

            selected_features = patient_df[['Dedos_amarillos', 'Ansiedad', 'Presión_de_pares', 'Enfermedad_crónica', 
                                            'Fatiga', 'Alergia', 'Sibilancias', 'Consumo_de_alcohol', 
                                            'Tos', 'Dificultad_para_tragar', 'Dolor_en_el_pecho']]
            selected_features.columns = selected_features.columns.str.replace(' ', '_')

            probability = lr_model.predict_proba(selected_features)[:, 1][0]

            patient_data_obj = PatientData(**patient_data)
            patient_data_obj.probability = probability
            patient_data_obj.save()

            probability_percentage = "{}%".format(int(round(probability * 100)))
            return render(request, 'result.html', {'probability': probability_percentage})
    else:
        form = PatientForm()
    return render(request, 'form.html', {'form': form})

# Vista de administración (solo para superusuarios)
@login_required
@user_passes_test(is_superuser)
def vistaAdmin(request):
    pacientes = PatientData.objects.all()

    genero_data = pacientes.values('Genero').annotate(count=Count('Genero'), avg_probabilidad=Avg('probability'))
    edad_data = pacientes.values('Edad').annotate(promedio_probabilidad=Avg('probability'))
    alcohol_data = pacientes.values('Consumo_de_alcohol').annotate(promedio_probabilidad=Avg('probability'))
    tos_probabilidad = pacientes.values('Tos').annotate(promedio_probabilidad=Avg('probability'))

    context = {
        'genero_data': json.dumps(list(genero_data)),
        'edad_data': json.dumps(list(edad_data)),
        'alcohol_data': json.dumps(list(alcohol_data)),
        'tos_probabilidad': json.dumps(list(tos_probabilidad)),
    }

    return render(request, 'admin/vistaAdmin.html', context)

# Vista para listar pacientes (solo para superusuarios)
@login_required
@user_passes_test(is_superuser)
def listar_pacientes(request):
    patients = PatientData.objects.all()
    return render(request, 'admin/listar_pacientes.html', {'patients': patients})

# Vista para eliminar pacientes (solo para superusuarios)
@login_required
@user_passes_test(is_superuser)
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(PatientData, pk=pk)
    paciente.delete()
    messages.success(request, "Paciente eliminado con éxito.")
    return redirect('listar_pacientes')

# Vista para listar usuarios (solo para superusuarios)
@login_required
@user_passes_test(is_superuser)
def listar_usuarios(request):
    usuarios = User.objects.filter(is_superuser=False)  # Filtra para excluir superusuarios
    return render(request, 'admin/listar_usuarios.html', {'usuarios': usuarios})

# Vista para eliminar usuario (solo para superusuarios)
@login_required
@user_passes_test(is_superuser)
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.delete()
    messages.success(request, "Usuario eliminado con éxito.")
    return redirect('listar_usuarios')

# Vista para descargar datos de pacientes en CSV (solo para superusuarios)
@login_required
@user_passes_test(is_superuser)
def descargar_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pacientes.csv"'
    writer = csv.writer(response)

    writer.writerow([
        'Nombre', 'Edad', 'Género', 'Dedos Amarillos', 'Ansiedad', 'Presión de Pares',
        'Enfermedad Crónica', 'Fatiga', 'Alergia', 'Sibilancias', 'Consumo de Alcohol',
        'Tos', 'Dificultad para Tragar', 'Dolor en el Pecho', 'Probabilidad de Cáncer'
    ])

    patients = PatientData.objects.all().values_list(
        'Nombre', 'Edad', 'Genero', 'Dedos_amarillos', 'Ansiedad', 'Presión_de_pares', 
        'Enfermedad_crónica', 'Fatiga', 'Alergia', 'Sibilancias', 'Consumo_de_alcohol', 
        'Tos', 'Dificultad_para_tragar', 'Dolor_en_el_pecho', 'probability'
    )
    for patient in patients:
        writer.writerow(patient)

    return response

# Vistas para restablecimiento de contraseña
def PasswordResetView(request):
    return render(request, 'PasswordResetView.html')

def PasswordResetConfirmView(request):
    return render(request, 'PasswordResetConfirmView.html')