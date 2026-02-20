from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cartelera', views.cartelera),
    path('horarios', views.horarios),
]
