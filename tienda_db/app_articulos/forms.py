from django import forms
from django.core import validators
from .models import Articulo


class ArticuloForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa el nombre del artículo'
        }),
        validators=[
            validators.MinLengthValidator(3, "El nombre es muy corto"),
            validators.RegexValidator(
                regex=r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ., -]+$',
                message="Solo se permiten letras y números"
            )
        ]
    )

    descripcion = forms.CharField(
        label="Descripción",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ingresa la descripción'
        }),
        validators=[
            validators.MaxLengthValidator(200, "La descripción es demasiado larga")
        ]
    )

    precio = forms.DecimalField(
        label="Precio",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    stock = forms.IntegerField(
        label="Stock",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    marca = forms.CharField(
        label="Marca",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    activo = forms.BooleanField(
        label="¿Activo?",
        required=False
    )

    class Meta:
        model = Articulo
        fields = '__all__'
