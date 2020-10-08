from django.forms import ModelForm
from .models import Post, Comentario



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'descripcion', 'contenido','imagen']


class ComentarioForm(ModelForm):

    class Meta:
        model = Comentario
        fields = ['autor', 'mensaje']