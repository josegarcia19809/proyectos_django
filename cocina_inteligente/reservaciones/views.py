from django.shortcuts import render
from django.db.models import Count, Avg, F, ExpressionWrapper, DurationField
from .models import Reservacion, Resena

def index(request):
    return render(request, "reservaciones/index.html")

# 🔥 1. Horas pico
def horas_pico(request):
    data = Reservacion.objects.values('hora_inicio') \
        .annotate(total=Count('id')) \
        .order_by('-total')

    return render(request, 'reservaciones/horas_pico.html', {'data': data})


# 📅 2. Reservaciones por día
def reservaciones_por_dia(request):
    data = Reservacion.objects.values('fecha') \
        .annotate(total=Count('id')) \
        .order_by('fecha')

    return render(request, 'reservaciones/por_dia.html', {'data': data})


# ❌ 3. Total por estado
def total_por_estado(request):
    data = Reservacion.objects.values('estado') \
        .annotate(total=Count('id'))

    return render(request, 'reservaciones/por_estado.html', {'data': data})


# 👥 4. Clientes frecuentes
def clientes_frecuentes(request):
    data = Reservacion.objects.values('cliente__nombre') \
        .annotate(total=Count('id')) \
        .order_by('-total')

    return render(request, 'reservaciones/clientes.html', {'data': data})


# 🪑 5. Mesas utilizadas
def mesas_utilizadas(request):
    data = Reservacion.objects.values('mesa__numero_mesa') \
        .annotate(total=Count('id')) \
        .order_by('-total')

    return render(request, 'reservaciones/mesas.html', {'data': data})


# ⏱️ 6. Tiempo promedio
def tiempo_promedio(request):
    duracion = ExpressionWrapper(
        F('hora_fin') - F('hora_inicio'),
        output_field=DurationField()
    )

    data = Reservacion.objects.aggregate(promedio=Avg(duracion))

    return render(request, 'reservaciones/tiempo.html', {'data': data})


# 👨‍👩‍👧 7. Promedio personas
def promedio_personas(request):
    data = Reservacion.objects.aggregate(promedio=Avg('numero_personas'))

    return render(request, 'reservaciones/promedio_personas.html', {'data': data})


# 📊 8. Por número de personas
def reservaciones_por_personas(request):
    data = Reservacion.objects.values('numero_personas') \
        .annotate(total=Count('id')) \
        .order_by('numero_personas')

    return render(request, 'reservaciones/por_personas.html', {'data': data})


# 🚫 9. No-shows
def no_shows(request):
    total = Reservacion.objects.filter(estado='no_show').count()

    return render(request, 'reservaciones/no_shows.html', {'total': total})


# 📈 10. Por día y estado
def reservaciones_por_dia_estado(request):
    data = Reservacion.objects.values('fecha', 'estado') \
        .annotate(total=Count('id')) \
        .order_by('fecha')

    return render(request, 'reservaciones/por_dia_estado.html', {'data': data})


# ⭐ 11. Promedio calificación
def promedio_calificacion(request):
    data = Resena.objects.aggregate(promedio=Avg('calificacion'))

    return render(request, 'reservaciones/calificacion.html', {'data': data})