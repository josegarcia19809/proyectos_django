from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def monthly_challenge(request, month):
    challenge_text = None

    if month == "january":
        challenge_text = "Enero: Organizar mis metas del año y establecer un plan de estudio claro."
    elif month == "february":
        challenge_text = "Febrero: Mejorar mis habilidades en programación practicando todos los días."
    elif month == "march":
        challenge_text = "Marzo: Desarrollar un pequeño proyecto web para reforzar lo aprendido."
    elif month == "april":
        challenge_text = "Abril: Leer un libro relacionado con tecnología o desarrollo personal."
    elif month == "may":
        challenge_text = "Mayo: Aprender una nueva herramienta o framework."
    elif month == "june":
        challenge_text = "Junio: Repasar estructuras de datos y algoritmos básicos."
    elif month == "july":
        challenge_text = "Julio: Crear una aplicación sencilla para practicar lógica."
    elif month == "august":
        challenge_text = "Agosto: Mejorar el diseño visual de mis proyectos."
    elif month == "september":
        challenge_text = "Septiembre: Practicar pruebas unitarias y buenas prácticas de código."
    elif month == "october":
        challenge_text = "Octubre: Optimizar un proyecto anterior aplicando mejoras."
    elif month == "november":
        challenge_text = "Noviembre: Documentar correctamente mis proyectos."
    elif month == "december":
        challenge_text = "Diciembre: Evaluar mis logros del año y planear nuevas metas."

    if challenge_text:
        return HttpResponse(challenge_text)
    else:
        return HttpResponseNotFound("Mes no válido")