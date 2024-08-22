from django.urls import path
from nutria_app import views

urlpatterns = [
    path ('', views.home_vista),
    path ('home/', views.home_vista),
    path('nutricionistas/', views.lista_nutricionistas, name='lista_nutricionistas'),
    path('nutricionistas/registrar/', views.registrar_nutricionista, name='registrar_nutricionista'),
    path('nutricionistas/<int:id>/', views.detalle_nutricionista, name='detalle_nutricionista'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/registrar/', views.registrar_paciente, name='registrar_paciente'),
    path('pacientes/<int:id>/', views.detalle_paciente, name='detalle_paciente'),
    path('sesiones/', views.lista_sesiones, name='lista_sesiones'),
    path('sesiones/registrar/', views.registrar_sesion, name='registrar_sesion'),
    path('sesiones/<int:id>/', views.detalle_sesion, name='detalle_sesion'),
]
