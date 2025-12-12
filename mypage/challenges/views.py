from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html",{
        'titulo': 'Tienda de productos',
        'subtitulo': 'Compra de verano'
    })

def productos(request):
    return render(request, "productos.html")