from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main_app.forms import RegisterForm

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
    register_form = RegisterForm()
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Registrado correctamente')

            return redirect('inicio')
    return render(request, 'users/register.html', {
        'title': 'Registro',
        'register_form': register_form,
    })
