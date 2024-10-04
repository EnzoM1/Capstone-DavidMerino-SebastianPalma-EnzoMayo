from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import lr_model, PatientData, Usuario
from .forms import PatientForm
from django.contrib import messages #esto tira los mensajes
import pandas as pd

#imports necesarios para que funcione la view

#ahora se llama login pa no confundir la vista

#en el mysql workspace pongan esto en su tabla "INSERT INTO `onco1`.`onco_usuario` (nombre, contra) VALUES ('skibidi', '12345');" para crealos de momento

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            usuario = Usuario.objects.get(nombre=username)  # Verifica que esto sea correcto
            if usuario.contra == password:  # Usa el nombre correcto del campo
                # Si las credenciales son correctas, redirige al usuario a otra página
                return redirect('form')  # Redirige al form  
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Nombre de usuario no encontrado.')
    
    return render(request, 'index.html')  # Asegúrate de que esta sea tu plantilla

def predict_probability(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient_data = form.cleaned_data
            # Crear un dataframe con los datos del paciente
            patient_df = pd.DataFrame([patient_data])
            # Seleccionar las características correctas
            selected_features = patient_df[['YELLOW_FINGERS', 'ANXIETY', 'PEER_PRESSURE', 'CHRONIC_DISEASE', 
                                 'FATIGUE', 'ALLERGY', 'WHEEZING', 'ALCOHOL_CONSUMING', 
                                 'COUGHING', 'SWALLOWING_DIFFICULTY', 'CHEST_PAIN','ANXYELFIN']]
            # Predecir la probabilidad de cáncer
            probability = lr_model.predict_proba(selected_features)[:, 1][0]
            # Convertir la probabilidad a porcentaje entero
            probability_percentage = "{}%".format(int(round(probability * 100)))
            
            
            #guardar los datos del paciente en un nuevo modelo y la base de datos
            patient_data_obj = PatientData(**patient_data)
            patient_data_obj.probability = probability_percentage
            patient_data_obj.save()
            
            return render(request, 'result.html', {'probability': probability_percentage})
    else:
        form = PatientForm()
    return render(request, 'form.html', {'form': form})



def PasswordResetView(request):
    return render(request, 'PasswordResetView.html')

def PasswordResetConfirmView(request):
    return render(request, 'PasswordResetConfirmView.html')