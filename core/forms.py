from django.forms import ModelForm
from django import forms
from .models import Business
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BusinessForm(ModelForm):
    class Meta:
            model = Business
            fields = ['nombre', 'lema', 'logo',
                      'email', 'direccion', 'telefonos', 'wpp',
                      'horarios','descripcion', 'mision', 'vision',
                      'historia']
