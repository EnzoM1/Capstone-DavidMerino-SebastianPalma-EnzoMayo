from django.shortcuts import render
from django.http import HttpResponse
from .models import lr_model, PatientData
from .forms import PatientForm
import pandas as pd

#imports necesarios para que funcione la view

def saludo(request):
    return render(request, 'index.html')

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