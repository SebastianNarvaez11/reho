from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from core.validators import *
from django.utils.timezone import now
# Create your models here.

def custom_upload_to(instance, filename):
    #primero evalua si existen instancias anteriores de el objeto a crear
    if not Post.objects.filter(pk=instance.pk):
        return 'posts/' + filename
    else:
        old_instance =  Post.objects.get(pk=instance.pk)
        old_instance.imagen.delete()
        return 'posts/' + filename


class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=50, unique=True, validators=[validate_only_letters, MinLengthValidator(3)])
    descripcion = models.TextField('Descripcion', max_length=200, blank=True, null=True)
    contenido = RichTextUploadingField('Contenido')
    imagen = models.ImageField('Imagen', upload_to=custom_upload_to) 
    # autor enlazado con los usuarios de django
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    slug = models.SlugField('Slug/Url')
    publicacion = models.DateField('Fecha de publicacion', default = now)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    edicion = models.DateField('Fecha de modificacion', auto_now=True)
    hora = models.DateTimeField('Hora creacion', auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = re.sub(r'[^a-z0-9+]', '-', self.titulo.lower())
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-hora']

    def __str__(self):
        return self.titulo



class Comentario(models.Model):
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField('Autor', max_length=200)
    mensaje = models.CharField('Mensaje', max_length=200)
    creacion = models.DateField('Fecha de creacion', auto_now_add=True)
    hora = models.DateTimeField('Hora creacion', auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        ordering = ['-hora']

    def __str__(self):
        return self.autor