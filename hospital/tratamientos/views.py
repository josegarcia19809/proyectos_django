from django.http import HttpResponse

layout = """
<hr>
<p>Hospital San Salud 🏥</p>
"""


def contacto_especialidad(request, nombre):
    return HttpResponse(f"""
        <h1>📞 Contacto de la especialidad: {nombre}</h1>
        <p>Para más información comunícate con el área correspondiente.</p>
    """ + layout)


def calificacion_especialidad(request, especialidad, calificacion):
    return HttpResponse(f"""
        <h1>⭐ Calificación de la especialidad</h1>
        <p>Especialidad: <strong>{especialidad}</strong></p>
        <p>Calificación: <strong>{calificacion}</strong></p>
    """ + layout)


def servicio_especialidad(request, especialidad="", costo=""):
    html = ""

    if especialidad and costo:
        html = f"""
            <h1>🩺 Servicio de la especialidad</h1>
            <p>Especialidad: <strong>{especialidad}</strong></p>
            <p>Costo del servicio: <strong>${costo}</strong></p>
        """
    else:
        html = """
            <p>⚠️ No se ha definido la especialidad o el costo del servicio.</p>
        """

    return HttpResponse(html + layout)
