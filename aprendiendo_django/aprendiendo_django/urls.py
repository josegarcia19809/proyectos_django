"""
URL configuration for aprendiendo_django project.

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
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("inicio/", views.index, name="inicio"),
    path("hola-mundo/", views.hola_mundo, name="hola_mundo"),
    path("adios-mundo/", views.adios_mundo, name="adios_mundo"),
    path("contacto/<str:nombre>", views.contacto, name="contacto"),
    path("calificacion/<str:asignatura>/<str:calificacion>",
         views.calificacion_asignatura, name="calificacion_asignatura"),
    path("precios/",
         views.producto_precio, name="producto_precio"),
    path("precios/<str:producto>/",
         views.producto_precio, name="producto_precio"),
    path("precios/<str:producto>/<str:precio>",
         views.producto_precio, name="producto_precio"),
    path("pagina/<int:redirigir>", views.pagina_redirigir, name="pagina_redirigir")
]
