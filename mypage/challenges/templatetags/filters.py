from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo(valor):
    return f"Hola {valor}"