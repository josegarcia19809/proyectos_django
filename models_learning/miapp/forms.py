from cProfile import label
from random import choices

from django import forms


class FormArticle(forms.Form):
    title = forms.CharField(
        label='Titulo',
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ingresa el Titulo'})
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea()
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
