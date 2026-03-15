from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
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
    "december": None
}

# Create your views here.
from django.http import HttpResponse


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months,
    })


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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month,
        })
    except:
        raise Http404()
