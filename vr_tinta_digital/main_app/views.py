from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main_app/index.html', {
        'title': 'Main App',
    })

def about(request):
    return render(request, 'main_app/about.html', {
        'title': 'Sobre nosotros',
    })

def register_page(request):
    return render(request, 'users/register.html', {
        'title': 'Registro',
    })