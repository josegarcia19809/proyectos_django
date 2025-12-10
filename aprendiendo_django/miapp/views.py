from django.http import HttpResponse
from django.shortcuts import render


layout="""
    <h1>Sitio web con Django | José L. García</h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio">Inicio</a>
        </li>
        <li>
            <a href="/hola-mundo">Hola Mundo</a>
        </li>
        <li>
            <a href="/adios-mundo">Adios Mundo</a>
        </li>

    </ul>
"""

# Create your views here.
def hola_mundo(request):
    return HttpResponse("""
    <h1>Hola mundo con Django!!!</h1>
    <h3>Bienvenido José García</h3>
    """+layout)


def adios_mundo(request):
    return HttpResponse("""
    <h1>Adios mundo 😍</h1>
    """+layout)


def index(request):
    html = """
    <h1>Página de inicio</h1>
    <p>Años hasta el 2050</p>
    <ul>
    """
    year = 2025
    while year <= 2050:
        if year %2 ==0:
            html += f"<li>{year}</li>"
        year = year + 1
    html += """</ul>"""+layout

    return HttpResponse(html)


def contacto(request, nombre):
    return HttpResponse(f"""
    <h1>Contacto 📞 {nombre}</h1>
    """+layout)

def calificacion_asignatura(request, asignatura, calificacion):
    return HttpResponse(f"""
    <h1>Calificación de la asignatura {asignatura}: {calificacion}</h1>
    """+layout)