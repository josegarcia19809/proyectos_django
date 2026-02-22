from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('comidas/', views.comidas, name='comidas'),
    path('bebidas/', views.bebidas, name='bebidas'),
]
