from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="inicio"),
    path('videojuego', views.videojuego, name="videojuego"),
    path('catalogo', views.catalogo, name="catalogo"),
    path('detalle/<int:id>', views.detalle, name="detalle"),
]
