from django.db import models


# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del artículo")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Cantidad en stock")
    marca = models.CharField(max_length=100, verbose_name="Marca")
    activo = models.BooleanField(default=True, verbose_name="¿Está activo?")
    imagen = models.ImageField(
        upload_to='articulos', verbose_name="Imagen",
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.marca}) - ${self.precio}"

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
