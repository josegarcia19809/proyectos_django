from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def comidas(request):
    return render(request, 'comidas.html')


def bebidas(request):
    return render(request, 'bebidas.html')
