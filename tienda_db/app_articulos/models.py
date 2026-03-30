from django.db import models


# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    marca = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
