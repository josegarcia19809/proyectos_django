from django.shortcuts import render


# Create your views here.

def index(request):
    cantidad = 10
    productos = ["TV", "Monitor", "Tablet"]
    years = range(2025, 2051)
    return render(request, "index.html", {
        'titulo': 'Tienda de productos',
        'subtitulo': 'Compra de verano',
        'cantidad': cantidad,
        'productos': productos,
        'years': years
    })


def productos(request):
    return render(request, "productos.html")
