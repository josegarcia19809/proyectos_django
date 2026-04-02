from django.http import HttpResponse
from django.shortcuts import render, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle


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


def ver_articulos_publicos(request):
    articulos = Article.objects.filter(public=True)
    return render(request, "articulos.html",
                  {"articulos": articulos})


def buscar_articulos_por_titulo(request):
    articulos = Article.objects.filter(title__contains="agua")
    return render(request, "articulos.html",
                  {"articulos": articulos})


def obtener_articulo_exacto(request):
    articulos = Article.objects.filter(
        title__exact="Cómo mejorar tu memoria fácilmente"
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def obtener_articulo_iexacto(request):
    articulos = Article.objects.filter(
        title__iexact="cómo mejorar tu memoria fácilmente"
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def obtener_articulos_mayor_id(request):
    articulos = Article.objects.filter(id__gt=5)
    return render(request, "articulos.html",
                  {"articulos": articulos})


def excluir_articulos_no_publicos(request):
    articulos = Article.objects.exclude(public=True)
    return render(request, "articulos.html",
                  {"articulos": articulos})


# Consultas con SQL
def obtener_articulos_raw(request):
    articulos = Article.objects.raw(
        "SELECT * FROM miapp_article WHERE public = 1"
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def obtener_articulos_raw_id(request):
    articulos = Article.objects.raw(
        "SELECT * FROM miapp_article WHERE id > 5"
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def excluir_articulos_raw(request):
    articulos = Article.objects.raw(
        "SELECT * FROM miapp_article WHERE public != 0"
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def buscar_articulos_q(request):
    articulos = Article.objects.filter(
        Q(title__icontains="agua") | Q(content__icontains="agua")
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def articulos_publicos_o_memoria(request):
    articulos = Article.objects.filter(
        Q(public=True) & Q(title__icontains="memoria")
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def excluir_con_q(request):
    articulos = Article.objects.filter(
        ~Q(title__icontains="agua")
    )
    return render(request, "articulos.html",
                  {"articulos": articulos})


def guardar_articulo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        public = request.POST.get("public")

        articulo = Article(
            title=title,
            content=content,
            public=public == "True",
        )
        articulo.save()
        return HttpResponse(
            f"Artículo creado: {articulo.title}, contenido: {articulo.content} ")
    else:
        return HttpResponse("<h2>No se podido crear el artículo</h2>")


def crear_articulo_form(request):
    return render(request, "crear_articulo.html", )


def crear_full_articulo(request):
    formulario = FormArticle
    return render(request, "full_articulo.html", {"formulario": formulario})