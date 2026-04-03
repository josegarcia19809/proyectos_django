from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='images/', default='null', verbose_name="Imagen")
    public = models.BooleanField(verbose_name="Publicado", default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Fecha de actualizacion")


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('-name',)
