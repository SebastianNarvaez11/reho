from django.db import models
import re
from ckeditor_uploader.fields import RichTextUploadingField
from core.validators import *
# Create your models here.

def custom_upload_to1(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Service.objects.filter(pk=instance.pk):
        return 'services/' + filename
    else:
        old_instance =  Service.objects.get(pk=instance.pk)
        old_instance.imagen1.delete()
        return 'services/' + filename
    
def custom_upload_to2(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Service.objects.filter(pk=instance.pk):
        return 'services/' + filename
    else:
        old_instance =  Service.objects.get(pk=instance.pk)
        old_instance.imagen2.delete()
        return 'services/' + filename


class Service(models.Model):
    titulo = models.CharField('Titulo', max_length=20, unique=True, validators=[MinLengthValidator(4)])
    slug = models.SlugField('Slug/Url')
    descripcion = models.CharField('Descripción', max_length=200)
    contenido = RichTextUploadingField('Contenido')
    imagen1 = models.ImageField('Imagen 1', upload_to=custom_upload_to1)
    imagen2 = models.ImageField('Imagen 2', upload_to=custom_upload_to2, null=True, blank=True)
    index = models.BooleanField('Mostrar en el inicio', default=True)
    estado = models.BooleanField('Publicado/Oculto', default=True)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    def save(self, *args, **kwargs):#genera el slug desde el titulo - importar re
        self.slug = re.sub(r'[^a-z0-9+]', '-', self.titulo.lower())
        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-creacion']

    def __str__(self):
        return self.titulo

