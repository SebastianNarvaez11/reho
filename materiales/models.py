from django.db import models
import re
from ckeditor_uploader.fields import RichTextUploadingField
from core.validators import *
# Create your models here.

def custom_upload_to1(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Material.objects.filter(pk=instance.pk):
        return 'materiales/' + filename
    else:
        old_instance =  Material.objects.get(pk=instance.pk)
        old_instance.imagen1.delete()
        return 'materiales/' + filename
    
def custom_upload_to2(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Material.objects.filter(pk=instance.pk):
        return 'materiales/' + filename
    else:
        old_instance =  Material.objects.get(pk=instance.pk)
        old_instance.imagen2.delete()
        return 'materiales/' + filename


class Material(models.Model):
    CATEGORIA_TYPE_CHOICES = (
        (1, 'Telas'),
        (2, 'Maderas'),
        (3, 'Pinturas'),)

    titulo = models.CharField('Titulo', max_length=20, unique=True, validators=[MinLengthValidator(4)])
    slug = models.SlugField('Slug/Url')
    descripcion = models.CharField('Descripción', max_length=150)
    contenido = RichTextUploadingField('Contenido')
    imagen1 = models.ImageField('Imagen 1', upload_to=custom_upload_to1)
    imagen2 = models.ImageField('Imagen 2', upload_to=custom_upload_to2, null=True, blank=True)
    categoria = models.PositiveSmallIntegerField('Categoria', choices=CATEGORIA_TYPE_CHOICES, default=1)
    index = models.BooleanField('Mostrar en el inicio', default=True)
    estado = models.BooleanField('Publicado/Oculto', default=True)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de edicion', auto_now=True)

    def save(self, *args, **kwargs):#genera el slug desde el titulo - importar re
        self.slug = re.sub(r'[^a-z0-9+]', '-', self.titulo.lower())
        super(Material, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiales'
        ordering = ['-creacion']

    def __str__(self):
        return self.titulo

