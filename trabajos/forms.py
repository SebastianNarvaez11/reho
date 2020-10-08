from django.forms import ModelForm
from django import forms
from .models import Trabajo


class TrabajoForm(ModelForm):

    class Meta:
        model = Trabajo
        fields = ['titulo', 'descripcion', 'contenido', 'imagen1', 'imagen2', 'imagen3', 'categoria', 'index', 'estado']
