from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hola_mundo(request):
    return HttpResponse("""
    <h1>Hola mundo con Django!!!</h1>
    <h3>Bienvenido José García</h3>
    """)


def adios_mundo(request):
    return HttpResponse("""
    <h1>Adios mundo 😍</h1>
    """)


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
    html += """</ul>"""

    return HttpResponse(html)
