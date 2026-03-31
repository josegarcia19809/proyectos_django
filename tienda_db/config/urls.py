"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_articulos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear-articulo/', views.crear_articulo, name='crear_articulo'),
    path('ver-articulo/', views.ver_articulo, name='ver_articulo'),
    path('editar-articulo/<int:id>/', views.editar_articulo, name='editar_articulo'),
    path('articulos/', views.ver_articulos, name='articulos'),
    path('borrar-articulo/<int:id>/', views.borrar_articulo, name='borrar_articulo'),
    # Ordenamiento
    path('articulos-ordenados/', views.ver_articulos_ordenados,
         name='articulos_ordenados'),

    # Límites
    path('articulos-limit/', views.ver_articulos_limit, name='articulos_limit'),
    path('articulos-rango/', views.ver_articulos_limit_rango, name='articulos_rango'),

    # Filtros
    path('articulos-activos/', views.ver_articulos_activos, name='articulos_activos'),
    path('buscar-articulos/', views.buscar_articulos_por_nombre, name='buscar_articulos'),
    path('articulo-exacto/', views.obtener_articulo_exacto, name='articulo_exacto'),
    path('articulo-iexacto/', views.obtener_articulo_iexacto, name='articulo_iexacto'),
    path('articulos-mayor-id/', views.obtener_articulos_mayor_id,
         name='articulos_mayor_id'),

    # Exclusión
    path('articulos-inactivos/', views.excluir_articulos_inactivos,
         name='articulos_inactivos'),

    # SQL RAW
    path('articulos-raw/', views.obtener_articulos_raw, name='articulos_raw'),
    path('articulos-raw-id/', views.obtener_articulos_raw_id, name='articulos_raw_id'),
    path('articulos-raw-excluir/', views.excluir_articulos_raw,
         name='articulos_raw_excluir'),

    # Consultas con Q
    path('articulos-q/', views.buscar_articulos_q, name='articulos_q'),
    path('articulos-activos-nombre/', views.articulos_activos_y_nombre,
         name='articulos_activos_nombre'),
    path('articulos-excluir-q/', views.excluir_con_q, name='articulos_excluir_q'),
]
