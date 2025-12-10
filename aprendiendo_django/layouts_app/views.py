from django.shortcuts import render

# Create your views here.

def layout_index(request):
    return render(request, "paginas.html")

def layout_productos(request):
    return render(request, "productos.html")