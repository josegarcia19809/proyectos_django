from django.shortcuts import render


def pedidos(request):
    return render(request, 'pedidos.html')


def confirmacion(request):
    return render(request, 'confirmacion.html')
