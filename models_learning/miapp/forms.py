from cProfile import label
from random import choices

from django import forms
from django.core import validators


class FormArticle(forms.Form):
    title = forms.CharField(
        label='Titulo',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa el Titulo'}),
        validators=[
            validators.MinLengthValidator(5, "El título es demasiado corto"),
            validators.RegexValidator(
                regex=r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ., -]+$',
                message="Solo se permiten letras y números"
            )
        ]
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea(),
        validators=[
            validators.MaxLengthValidator(25, "El contenido es demasiado largo"),
            validators.RegexValidator(
                regex=r'^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ., -]+$',
                message="Solo se permiten letras y números"
            )
        ]
    )
    content.widget.attrs.update(
        {'class': 'form-control',
         'placeholder': 'Ingresa el Contenido'})

    public_options = [
        (1, 'Si'),
        (0, 'No'),
    ]

    public = forms.TypedChoiceField(
        label='Publicado?',
        choices=public_options
    )
