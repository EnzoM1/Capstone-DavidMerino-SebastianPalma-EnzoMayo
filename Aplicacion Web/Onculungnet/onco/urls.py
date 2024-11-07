from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#tema urls en el futuro protegerlas para que no ingresen escribiendola manual

urlpatterns = [

    path('',views.pagina_inicio,name="pagina_inicio"),

    path('inicioSesion/',views.inicioSesion,name="inicioSesion"),

    path('sintomas/',views.sintomas,name="sintomas"),

    path('form/',views.predict_probability, name="form"), 
    
    # URL para solicitar el restablecimiento de contraseña
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    # URL que se muestra cuando el email ha sido enviado
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    
    # URL para ingresar una nueva contraseña, incluye el token único que Django genera
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # URL que confirma que la contraseña ha sido cambiada exitosamente
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('logout/',views.cerrarSesion,name="logout"),

    #admin view
    path('vistaAdmin/',views.vistaAdmin, name="vistaAdmin"),
    path('register/',views.register, name="register"),
    path('listar_pacientes/', views.listar_pacientes, name='listar_pacientes'),
    path('descargar_csv/', views.descargar_csv, name='descargar_csv'),
]