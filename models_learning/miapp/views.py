from django.http import HttpResponse
from django.shortcuts import render, redirect
from miapp.models import Article


# Create your views here.

def crear_articulo(request):
    articulo = Article(
        title='Articulo de la vista',
        content='Content de la vista',
        public=True,

    )
    articulo.save()
    return HttpResponse(
        f"Artículo creado: {articulo.title}, contenido: {articulo.content} ")


def crear_articulo2(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public,

    )
    articulo.save()
    return HttpResponse(
        f"Artículo creado: {articulo.title}, contenido: {articulo.content} ")


def ver_articulo(request):
    try:
        articulo = Article.objects.get(title='Coca Cola')
        response = f"articulo {articulo.title}, contenido: {articulo.content}"
    except:
        response = "<h1>Articulo no existe</h1>"
    return HttpResponse(response)


def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.title = "Leche en polvo"
    articulo.content = "Presentación familiar"
    articulo.public = True

    articulo.save()
    return HttpResponse(
        f"Artículo modificado: {articulo.title}, contenido: {articulo.content} ")


def ver_articulos(request):
    articulos = Article.objects.all()
    return render(request, "articulos.html",
                  {"articulos": articulos})


def ver_articulos_ordenados(request):
    articulos = Article.objects.order_by("-title")  # forma descendente
    return render(request, "articulos.html",
                  {"articulos": articulos})


def ver_articulos_limit(request):
    articulos = Article.objects.order_by("title")[:3]  # Los 3 primeros
    return render(request, "articulos.html",
                  {"articulos": articulos})


def ver_articulos_limit_rango(request):
    articulos = Article.objects.order_by("title")[3:7]  # del índice 3 al 6
    return render(request, "articulos.html",
                  {"articulos": articulos})


def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect("articulos")

