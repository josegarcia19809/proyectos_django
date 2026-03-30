from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_articulos.models import Articulo


def crear_articulo(request):
    articulo = Articulo(
        nombre='Coca Cola',
        descripcion='Refresco de 600ml',
        precio=18.50,
        stock=100,
        marca='Coca Cola',
        activo=True
    )
    articulo.save()

    return HttpResponse(
        f"Artículo creado: {articulo.nombre}, precio: {articulo.precio}"
    )


def ver_articulo(request):
    try:
        articulo = Articulo.objects.get(nombre='Coca Cola')
        response = (f"Artículo: {articulo.nombre}, precio: {articulo.precio}, "
                    f"stock: {articulo.stock}")
    except Articulo.DoesNotExist:
        response = "<h1>Artículo no existe</h1>"

    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)

    articulo.nombre = "Leche en polvo"
    articulo.descripcion = "Presentación familiar"
    articulo.precio = 120.00
    articulo.stock = 50
    articulo.marca = "Nestlé"
    articulo.activo = True

    articulo.save()

    return HttpResponse(
        f"Artículo modificado: {articulo.nombre}, precio: {articulo.precio}"
    )


def ver_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, "articulos.html", {"articulos": articulos})


def borrar_articulo(request, id):
    articulo = Articulo.objects.get(pk=id)
    articulo.delete()
    return redirect("articulos")