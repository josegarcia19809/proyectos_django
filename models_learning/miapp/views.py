from django.http import HttpResponse
from django.shortcuts import render
from miapp.models import Article


# Create your views here.

def crear_articulo(request):
    articulo = Article(
        title='Articulo de la vista',
        content='Content de la vista',
        public=True,

    )
    articulo.save()
    return HttpResponse("Crear articulo")
