from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedidos, name='pedidos'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
]
