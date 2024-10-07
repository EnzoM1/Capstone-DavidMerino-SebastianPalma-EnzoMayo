from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#tema urls en el futuro protegerlas para que no ingresen escribiendola manual

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('form/',views.predict_probability, name="form"), 
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # Vista que informa al usuario que se ha enviado un correo
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  
    # Vista que contiene el formulario para restablecer la contraseña usando el token enviado
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Vista que informa al usuario que la contraseña ha sido restablecida exitosamente
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/',views.cerrarSesion,name="logout"),

    #admin view
    path('vistaAdmin/',views.vistaAdmin, name="vistaAdmin"),
    path('register/',views.register, name="register"),
]