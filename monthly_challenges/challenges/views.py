from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def january(request):
    return HttpResponse("Enero: Organizar mis metas del año y establecer un plan de estudio claro.")

def february(request):
    return HttpResponse("Febrero: Mejorar mis habilidades en programación practicando todos los días.")

def march(request):
    return HttpResponse("Marzo: Desarrollar un pequeño proyecto web para reforzar lo aprendido.")

def april(request):
    return HttpResponse("Abril: Leer un libro relacionado con tecnología o desarrollo personal.")

def may(request):
    return HttpResponse("Mayo: Aprender una nueva herramienta o framework.")

def june(request):
    return HttpResponse("Junio: Repasar estructuras de datos y algoritmos básicos.")

def july(request):
    return HttpResponse("Julio: Crear una aplicación sencilla para practicar lógica.")

def august(request):
    return HttpResponse("Agosto: Mejorar el diseño visual de mis proyectos.")

def september(request):
    return HttpResponse("Septiembre: Practicar pruebas unitarias y buenas prácticas de código.")

def october(request):
    return HttpResponse("Octubre: Optimizar un proyecto anterior aplicando mejoras.")

def november(request):
    return HttpResponse("Noviembre: Documentar correctamente mis proyectos.")

def december(request):
    return HttpResponse("Diciembre: Evaluar mis logros del año y planear nuevas metas.")