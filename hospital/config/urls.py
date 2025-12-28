"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doctores import views as doctores_views
from tratamientos import views as tratam_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_doctores/', doctores_views.index_doctores, name='index_doctores'),
    path('doctores/sistema_medico/', doctores_views.sistema_medico,
         name='sistema_medico'),
    path('doctores/pacientes/', doctores_views.pacientes_doctor, name='pacientes_doctor'),
    path('doctores/citas/', doctores_views.citas_medicas, name='citas_medicas'),
    path('doctores/historial/', doctores_views.historial_clinico,
         name='historial_clinico'),
    path('doctores/recetas/', doctores_views.recetas_medicas, name='recetas_medicas'),
    path('doctores/emergencias/', doctores_views.emergencias, name='emergencias'),

    # Información de contacto de una especialidad
    path(
        "especialidad/contacto/<str:nombre>/",
        tratam_views.contacto_especialidad,
        name="contacto_especialidad"
    ),

    # Calificación de una especialidad
    path(
        "especialidad/calificacion/<str:especialidad>/<str:calificacion>/",
        tratam_views.calificacion_especialidad,
        name="calificacion_especialidad"
    ),

    # Servicios de una especialidad
    path(
        "especialidad/servicios/",
        tratam_views.servicio_especialidad,
        name="servicio_especialidad"
    ),
    path(
        "especialidad/servicios/<str:especialidad>/",
        tratam_views.servicio_especialidad,
        name="servicio_especialidad"
    ),
    path(
        "especialidad/servicios/<str:especialidad>/<str:costo>/",
        tratam_views.servicio_especialidad,
        name="servicio_especialidad"
    ),
]
