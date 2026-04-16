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
from miapp import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("crear-articulo/", views.crear_articulo, name="crear_articulo"),
    path("crear-articulo2/<str:title>/<str:content>/<str:public>", views.crear_articulo2,
         name="crear_articulo2"),
    path("ver-articulo/", views.ver_articulo, name="ver_articulo"),
    path("editar-articulo/<int:id>/", views.editar_articulo, name="editar_articulo"),
    path("articulos/", views.ver_articulos, name="articulos"),
    path("articulos-ordenados/", views.ver_articulos_ordenados,
         name="articulos_ordenados"),
    path("articulos-limite/", views.ver_articulos_limit, name="articulos_limite"),
    path("articulos-limite-rango/", views.ver_articulos_limit_rango,
         name="articulos_limite_rango"),
    path("borrar-articulo/<int:id>/", views.borrar_articulo, name="borrar_articulo"),
    path("articulos-publicos/", views.ver_articulos_publicos, name="articulos_publicados"),
    path("articulos/buscar/", views.buscar_articulos_por_titulo, name="buscar_articulos"),
    path("articulos/exacto/", views.obtener_articulo_exacto, name="articulo_exacto"),
    path("articulos/iexacto/", views.obtener_articulo_iexacto, name="articulo_iexacto"),
    path("articulos/mayor-id/", views.obtener_articulos_mayor_id,
         name="articulos_mayor_id"),
    path("articulos/excluir/", views.excluir_articulos_no_publicos,
         name="excluir_articulos"),
    path("articulos/raw/", views.obtener_articulos_raw, name="articulos_raw"),
    path("articulos/raw-id/", views.obtener_articulos_raw_id, name="articulos_raw_id"),
    path("articulos/raw-excluir/", views.excluir_articulos_raw,
         name="articulos_raw_excluir"),
    path("articulos/q/", views.buscar_articulos_q, name="articulos_q"),
    path("articulos/q2/", views.articulos_publicos_o_memoria, name="articulos_q2"),
    path("articulos/q-excluir/", views.excluir_con_q, name="articulos_q_excluir"),
    path("guardar-articulo/", views.guardar_articulo, name="guardar_articulo"),
    path("crear-articulo-form/", views.crear_articulo_form, name="crear_articulo_form"),
    path("crear-articulo-form-full/", views.crear_full_articulo,
         name="crear_full_articulo"),
]

# Configurar el titulo del panel
admin.site.site_header = "Tienda de artículos"


# Configuración para cargar imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
