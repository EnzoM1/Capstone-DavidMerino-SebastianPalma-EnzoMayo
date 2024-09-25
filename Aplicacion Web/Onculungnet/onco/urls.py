from django.urls import path
from . import views

#tema urls en el futuro protegerlas para que no ingresen escribiendola manual

urlpatterns = [
    path('',views.saludo),
    path('form/',views.predict_probability, name="form"), 
]