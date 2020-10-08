from django.forms import ModelForm
from django import forms
from .models import Material


class MaterialForm(ModelForm):

    class Meta:
        model = Material
        fields = ['titulo', 'descripcion', 'contenido', 'imagen1', 'imagen2', 'imagen3', 'categoria', 'index', 'estado']
