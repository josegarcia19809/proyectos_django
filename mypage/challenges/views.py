from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    cantidad = 10
    lista_productos = ["TV", "Monitor", "Tablet"]
    years = range(2025, 2051)
    nombre = "José García"
    return render(request, "index.html", {
        'titulo': 'Tienda de productos',
        'subtitulo': 'Compra de verano',
        'cantidad': cantidad,
        'lista_productos': lista_productos,
        'years': years,
        'nombre': nombre
    })


def productos(request):
    return render(request, "productos.html")

def producto_precio(request, producto="", precio=""):
    html = ""
    if producto and precio:
        html = f"<h1>Precio del producto {producto}: ${precio}</h1>"
    else:
        html = "<p> No se han definido nombre del producto o su precio</p>"
    return HttpResponse(html)
