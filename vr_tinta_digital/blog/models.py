from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripcion")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(
        upload_to='articles', verbose_name="Imagen",
        null=True, blank=True
    )
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, verbose_name="Usuario",
                             editable=False, 
                             on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías",
                                        blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Fecha de creacion")
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"

    def __str__(self):
        return self.title
