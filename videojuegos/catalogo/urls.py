from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('videojuego', views.videojuego),
    path('catalogo', views.catalogo),
    path('detalle/<int:id>', views.detalle),
]
