from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('horas-pico/', views.horas_pico),
    path('por-dia/', views.reservaciones_por_dia),
    path('por-estado/', views.total_por_estado),
    path('clientes/', views.clientes_frecuentes),
    path('mesas/', views.mesas_utilizadas),
    path('tiempo-promedio/', views.tiempo_promedio),
    path('promedio-personas/', views.promedio_personas),
    path('por-personas/', views.reservaciones_por_personas),
    path('no-shows/', views.no_shows),
    path('por-dia-estado/', views.reservaciones_por_dia_estado),
    path('promedio-calificacion/', views.promedio_calificacion),
]