from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def cartelera(request):
    return render(request, 'cartelera.html')


def horarios(request):
    return render(request, 'horarios.html')
