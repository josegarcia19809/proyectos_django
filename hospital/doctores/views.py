from django.shortcuts import render, HttpResponse

# Create your views here.

def index_doctores(request):
    return HttpResponse("Hola, mundo. Bienvenido Doctor! 👨‍⚕️")

# Página principal para doctores
def sistema_medico(request):
    return HttpResponse("""
        <h1>👨‍⚕️ Sistema Médico</h1>
        <p>Bienvenido Doctor al sistema de gestión hospitalaria.</p>
        <p>Desde aquí podrá acceder a sus pacientes y consultas.</p>
    """)


# Vista de pacientes
def pacientes_doctor(request):
    return HttpResponse("""
        <h1>🧑‍🤝‍🧑 Pacientes</h1>
        <h2>Listado de pacientes</h2>
        <p>Consulta la información clínica de tus pacientes.</p>
        <p>Accede al historial médico y diagnósticos.</p>
    """)

# Vista de citas médicas
def citas_medicas(request):
    return HttpResponse("""
        <h1>📅 Citas Médicas</h1>
        <h2>Agenda del doctor</h2>
        <p>Revisa tus citas programadas.</p>
        <p>Organiza consultas presenciales y virtuales.</p>
    """)

# Vista de historial clínico
def historial_clinico(request):
    return HttpResponse("""
        <h1>📋 Historial Clínico</h1>
        <h2>Información médica</h2>
        <p>Consulta diagnósticos previos.</p>
        <p>Revisa tratamientos y resultados.</p>
    """)

# Vista de recetas médicas
def recetas_medicas(request):
    return HttpResponse("""
        <h1>💊 Recetas Médicas</h1>
        <h2>Prescripción de medicamentos</h2>
        <p>Crea y consulta recetas para tus pacientes.</p>
        <p>Controla dosis y duración del tratamiento.</p>
    """)

# Vista de emergencias
def emergencias(request):
    return HttpResponse("""
        <h1>🚑 Emergencias</h1>
        <h2>Atención prioritaria</h2>
        <p>Acceso rápido a pacientes en estado crítico.</p>
        <p>Protocolos de actuación inmediata.</p>
    """)
