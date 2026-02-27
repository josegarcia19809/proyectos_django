from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render

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


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Mes no válido")

    redirect_month = months[int(month) - 1]
    return HttpResponseRedirect(f"/challenges/{redirect_month}")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Mes no válido")
