from django.forms import ModelForm
from django import forms
from .models import Service


class ServiceForm(ModelForm):

    class Meta:
        model = Service
        fields = ['titulo', 'descripcion', 'contenido', 'imagen1', 'imagen2', 'imagen3', 'index', 'estado']
