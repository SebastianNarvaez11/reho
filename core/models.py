from django.db import models
from .validators import *
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Business(models.Model):
    nombre = models.CharField('Nombre', max_length=30, validators=[validate_only_letters, MinLengthValidator(7)])
    lema = models.CharField('Lema', max_length=50, validators=[validate_only_letters, MinLengthValidator(7)])
    logo = models.ImageField('Logo', upload_to='business', blank=True, null=True)
    email = models.EmailField('Email', max_length=254)
    direccion = models.CharField('Dirección', max_length=30, validators=[MinLengthValidator(7)])
    telefonos = models.CharField('Telefonos', max_length=50, validators=[validate_only_numbers, MinLengthValidator(5)])
    wpp = models.CharField('Whatsapp', max_length=50, validators=[validate_only_numbers, MinLengthValidator(5)])
    horarios = models.CharField('Horarios', max_length=100, validators=[MinLengthValidator(2)])
    descripcion = RichTextUploadingField('Descripcion')
    mision = RichTextUploadingField('Misión')
    vision = RichTextUploadingField('Vision')
    historia = RichTextUploadingField('Historia')
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre



