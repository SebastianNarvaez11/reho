from django.forms import ModelForm
from django import forms
from .models import Producto


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['titulo', 'descripcion', 'contenido', 'imagen1', 'imagen2',
                  'imagen3', 'imagen4', 'categoria', 'valor', 'index', 'estado']
