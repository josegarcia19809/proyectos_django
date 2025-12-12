from django.shortcuts import render

# Create your views here.

def index(request):
    cantidad =10
    return render(request, "index.html",{
        'titulo': 'Tienda de productos',
        'subtitulo': 'Compra de verano',
        'cantidad': cantidad
    })

def productos(request):
    return render(request, "productos.html")