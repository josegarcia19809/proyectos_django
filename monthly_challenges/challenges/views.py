from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    "january": "Enero: Organizar mis metas del año y establecer un plan de estudio claro.",
    "february": "Febrero: Mejorar mis habilidades en programación practicando todos los días.",
    "march": "Marzo: Desarrollar un pequeño proyecto web para reforzar lo aprendido.",
    "april": "Abril: Leer un libro relacionado con tecnología o desarrollo personal.",
    "may": "Mayo: Aprender una nueva herramienta o framework.",
    "june": "Junio: Repasar estructuras de datos y algoritmos básicos.",
    "july": "Julio: Crear una aplicación sencilla para practicar lógica.",
    "august": "Agosto: Mejorar el diseño visual de mis proyectos.",
    "september": "Septiembre: Practicar pruebas unitarias y buenas prácticas de código.",
    "october": "Octubre: Optimizar un proyecto anterior aplicando mejoras.",
    "november": "Noviembre: Documentar correctamente mis proyectos.",
    "december": "Diciembre: Evaluar mis logros del año y planear nuevas metas."
}

# Create your views here.
from django.http import HttpResponse


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Mes no válido")

    redirect_month = months[int(month) - 1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Mes no válido")
