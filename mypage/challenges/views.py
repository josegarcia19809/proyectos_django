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
