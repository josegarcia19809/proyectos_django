from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_articulos.models import Articulo
from django.db.models import Q
from .forms import ArticuloForm


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


def ver_articulos_ordenados(request):
    articulos = Articulo.objects.order_by("-nombre")
    return render(request, "articulos.html", {"articulos": articulos})


# 🔹 Límites

def ver_articulos_limit(request):
    articulos = Articulo.objects.order_by("nombre")[:3]
    return render(request, "articulos.html", {"articulos": articulos})


def ver_articulos_limit_rango(request):
    articulos = Articulo.objects.order_by("nombre")[3:7]
    return render(request, "articulos.html", {"articulos": articulos})


# 🔹 Filtros

def ver_articulos_activos(request):
    articulos = Articulo.objects.filter(activo=True)
    return render(request, "articulos.html", {"articulos": articulos})


def buscar_articulos_por_nombre(request):
    articulos = Articulo.objects.filter(nombre__contains="lata")
    return render(request, "articulos.html", {"articulos": articulos})


def obtener_articulo_exacto(request):
    articulos = Articulo.objects.filter(nombre__exact="Coca Cola 600ml")
    return render(request, "articulos.html", {"articulos": articulos})


def obtener_articulo_iexacto(request):
    articulos = Articulo.objects.filter(nombre__iexact="coca cola 600ml")
    return render(request, "articulos.html", {"articulos": articulos})


def obtener_articulos_mayor_id(request):
    articulos = Articulo.objects.filter(id__gt=5)
    return render(request, "articulos.html", {"articulos": articulos})


# 🔹 Exclusión

def excluir_articulos_inactivos(request):
    articulos = Articulo.objects.exclude(activo=True)
    return render(request, "articulos.html", {"articulos": articulos})


# 🔹 SQL RAW

def obtener_articulos_precio_caro(request):
    articulos = Articulo.objects.raw(
        "SELECT * FROM app_articulos_articulo WHERE precio > 50"
    )
    return render(request, "articulos.html", {"articulos": articulos})


def obtener_articulos_id_mayor5(request):
    articulos = Articulo.objects.raw(
        "SELECT * FROM app_articulos_articulo WHERE id > 5"
    )
    return render(request, "articulos.html", {"articulos": articulos})


def obtener_articulos_activos(request):
    articulos = Articulo.objects.raw(
        "SELECT * FROM app_articulos_articulo WHERE activo = 1"
    )
    return render(request, "articulos.html", {"articulos": articulos})


# 🔹 Consultas con Q

def buscar_articulos_q(request):
    articulos = Articulo.objects.filter(
        Q(nombre__icontains="1kg") | Q(descripcion__icontains="agua")
    )
    return render(request, "articulos.html", {"articulos": articulos})


def articulos_activos_y_nombre(request):
    articulos = Articulo.objects.filter(
        Q(activo=True) & Q(nombre__icontains="leche")
    )
    return render(request, "articulos.html", {"articulos": articulos})


def excluir_con_q(request):
    articulos = Articulo.objects.filter(
        ~Q(nombre__icontains="1kg")
    )
    return render(request, "articulos.html", {"articulos": articulos})


def formulario_manual(request):
    return render(request, "articulo_form_manual.html")


def guardar_articulo(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        stock = request.POST.get("stock")
        marca = request.POST.get("marca")
        activo = request.POST.get("activo") == "True"

        Articulo.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            marca=marca,
            activo=activo
        )

        return redirect("articulos")


def formulario_django(request):
    if request.method == "POST":
        formulario = ArticuloForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("articulos")
    else:
        formulario = ArticuloForm()

    return render(request, "articulo_form.html", {"formulario": formulario})
