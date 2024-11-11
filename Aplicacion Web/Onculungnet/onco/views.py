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
import google.generativeai as genai
import os


# instala pip install -q -U google-generativeai

#imports necesarios para que funcione la view

#ahora se llama login pa no confundir la vista

#de momento el register se puede entrar sin necesidad de iniciar, tienen que crear el usuario "skibidi" la contra la que sea y iniciado con el skibidi en la url ponen /vistaAdmin

#si entran con otro usuario osea crean otro cualquiera y intentan ingresar a /vistaAdmin no van a tener acceso





#views mas ordenadas

#AIzaSyAqvNh3fErKA8opsQDv85cbKlrwbclBQ18

#super user es OncoAdmin clave : admin --mejorar con algun generador

# Configurar la API de OpenAI
# Configura la clave API de Gemini
os.environ["GEMINI_API_KEY"] = "AIzaSyDIkyPjiGOslUXJT8wqSwKe8ZHd4bDfamU"

genai.configure(api_key=os.environ["GEMINI_API_KEY"])





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

# Función para interpretar la probabilidad usando Gemini
def interpret_probability_with_gemini(probability):
    #prompt = (
     #   f"Un modelo de predicción ha calculado una probabilidad de {probability*100}% para un paciente "
      #  "en relación al cáncer de pulmón. Como experto en salud, ¿puedes explicar qué significa esta probabilidad "
       # "en términos de riesgo de cáncer de pulmón? ¿Cuáles son las recomendaciones y qué medidas adicionales se deben tomar?"
    #)

    # Llamada a la API de Gemini para generar la interpretación
    #response = genai.generate_text(  # Cambiar generate_text por generate_content
     #   model="gemini-1.5-flash",
      #  prompt=prompt,
       # max_tokens=100,
        #temperature=0.7,
    #)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Un modelo de predicción ha calculado una probabilidad de {probability*100}% para un paciente "
        "en relación al cáncer de pulmón. Como experto en salud"
        "en términos de riesgo de cáncer de pulmón? ¿Cuáles son las recomendaciones y qué medidas adicionales se deben tomar?"
        "que sea breve, solo destacar los mas importante, ya que esto no es un modelo 100% preciso")  

    interpretation = response.text
    return interpretation

# Vista para predecir la probabilidad de cáncer (solo para usuarios autenticados)
@login_required
def predict_probability(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_data = form.cleaned_data
            patient_df = pd.DataFrame([patient_data])

            # Preprocesar las características seleccionadas
            selected_features = patient_df[['Dedos_amarillos', 'Ansiedad', 'Presión_de_pares', 'Enfermedad_crónica',
                                            'Fatiga', 'Alergia', 'Sibilancias', 'Consumo_de_alcohol',
                                            'Tos', 'Dificultad_para_tragar', 'Dolor_en_el_pecho']]
            selected_features.columns = selected_features.columns.str.replace(' ', '_')

            # Realizar la predicción
            probability = lr_model.predict_proba(selected_features)[:, 1][0]
            patient_data_obj = PatientData(**patient_data)
            patient_data_obj.probability = probability
            patient_data_obj.save()

            # Obtener la interpretación de la probabilidad usando Gemini
            interpretation = interpret_probability_with_gemini(probability)

            # Mostrar el resultado y la interpretación
            probability_percentage = "{}%".format(int(round(probability * 100)))
            return render(request, 'result.html', {
                'probability': probability_percentage,
                'interpretation': interpretation
            })
    else:
        form = PatientForm()

    return render(request, 'form.html', {'form': form})

# Función para generar la interpretación de datos con Gemini
def interpret_graph_data_with_gemini(data):
    data_str = json.dumps(data)  # Convertir los datos a string JSON
    prompt = (
        f"Se tienen los siguientes datos sobre las probabilidades de cáncer de pulmón en pacientes: {data_str}. "
        "Como experto en salud, ¿qué conclusiones puedes sacar de estos datos? "
        "¿Hay alguna tendencia relevante que deba preocupar a los médicos o pacientes?"
    )

    # Llamada a la API usando Gemini
    #response = genai.generate_content(  # Cambiar generate_text por generate_content
     #   model="gemini-1.5-flash",
      #  prompt=prompt,
       # max_tokens=100,
        #temperature=0.7,
    #)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Se tienen los siguientes datos sobre las probabilidades de cáncer de pulmón en pacientes: {data_str}. "
        "Como experto en salud, ¿qué conclusiones puedes sacar de estos datos? "
        "¿Hay alguna tendencia relevante que deba preocupar a los médicos o pacientes?"
        "que sea breve solo destacar lo importante")

    interpretation = response.text
    return interpretation

# Vista de administración (solo para superusuarios)
@login_required
@user_passes_test(is_superuser)
def vistaAdmin(request):
    pacientes = PatientData.objects.all()

    # Obtener los datos agregados para los gráficos
    genero_data = pacientes.values('Genero').annotate(count=Count('Genero'), avg_probabilidad=Avg('probability'))
    edad_data = pacientes.values('Edad').annotate(promedio_probabilidad=Avg('probability'))
    alcohol_data = pacientes.values('Consumo_de_alcohol').annotate(promedio_probabilidad=Avg('probability'))
    tos_probabilidad = pacientes.values('Tos').annotate(promedio_probabilidad=Avg('probability'))

    # Convertir los QuerySets en listas para pasarlos a JSON
    genero_data_list = list(genero_data)
    edad_data_list = list(edad_data)
    alcohol_data_list = list(alcohol_data)
    tos_probabilidad_list = list(tos_probabilidad)

    # Interpretación automática usando Gemini
    genero_analysis = interpret_graph_data_with_gemini(genero_data_list)
    edad_analysis = interpret_graph_data_with_gemini(edad_data_list)
    alcohol_analysis = interpret_graph_data_with_gemini(alcohol_data_list)
    tos_analysis = interpret_graph_data_with_gemini(tos_probabilidad_list)

    # Pasar los datos y análisis a la plantilla
    context = {
        'genero_data': json.dumps(genero_data_list),
        'edad_data': json.dumps(edad_data_list),
        'alcohol_data': json.dumps(alcohol_data_list),
        'tos_probabilidad': json.dumps(tos_probabilidad_list),
        'genero_analysis': genero_analysis,
        'edad_analysis': edad_analysis,
        'alcohol_analysis': alcohol_analysis,
        'tos_analysis': tos_analysis,
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