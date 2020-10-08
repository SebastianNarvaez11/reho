from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponseRedirect
from .models import Post, Comentario
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PostForm, ComentarioForm
from django.urls import reverse_lazy
from django.contrib import messages
from contact.forms import SuscribeForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def blog(request):
    queryset = request.GET.get("buscar")
    lista_posts = Post.objects.all()
    if queryset:
        lista_posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    paginator = Paginator(lista_posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    suscribe_form = SuscribeForm()
    if request.method == "POST":
        # Optiene los datos del formulario
        suscribe_form = SuscribeForm(data=request.POST)
        if suscribe_form.is_valid():
            asunto = 'Solicitud de Suscripcion'
            email = request.POST.get('email', '')
            contenido = 'Hola, me gustaria suscribirme a su lista de correos electronicos'
            # ENVIAMOS EL CORREO
            email = EmailMessage(
                "Sitio Web - {}".format(asunto),  # Asunto del mensaje
                "Email: <{}> \n\nEscribio: \n\n{} ".format(
                    email, contenido),  # estructura del mensaje
                "testing.developer.404@gmail.com",  # email de origen
                ["narvaez.jhoan@correounivalle.edu.co"],  # email de destino
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('blog')+"?ok")
            except:
                return redirect(reverse('blog')+"?fail")

    return render(request, 'blog/blog.html', {'lista_posts': lista_posts, 'posts': posts, 'formulario': suscribe_form})


def detallepost(request, slug_post):
    queryset = request.GET.get("buscar")
    lista_posts = Post.objects.all()
    if queryset:
        lista_posts = Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()
        paginator = Paginator(lista_posts, 2)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'blog/blog.html', {'lista_posts': lista_posts, 'posts': posts})

    post = get_object_or_404(Post, slug=slug_post)
    posts = Post.objects.all()

    suscribe_form = SuscribeForm()
    if request.method == "POST":
        # Optiene los datos del formulario
        suscribe_form = SuscribeForm(data=request.POST)
        if suscribe_form.is_valid():
            asunto = 'Solicitud de Suscripcion'
            email = request.POST.get('email', '')
            contenido = 'Hola, me gustaria suscribirme a su lista de correos electronicos'
            # ENVIAMOS EL CORREO
            email = EmailMessage(
                "Sitio Web - {}".format(asunto),  # Asunto del mensaje
                "Email: <{}> \n\nEscribio: \n\n{} ".format(
                    email, contenido),  # estructura del mensaje
                "testing.developer.404@gmail.com",  # email de origen
                ["narvaez.jhoan@correounivalle.edu.co"],  # email de destino
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('blog')+"?ok")
            except:
                return redirect(reverse('blog')+"?fail")

    return render(request, 'blog/detallepost.html', {'post': post, 'lista_posts': posts, 'formulario': suscribe_form})


######## Vistas Del Dashboard Post #########################
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post

    # filtra el el queryset por autor, solo podra ver los post que sean de su propiedad
    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)


@method_decorator(login_required, name='dispatch')
class PostCreateView(SinPermisos, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog_dash:list')
    success_message = "Post creado satisfactoriamente"

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostUpdateView(SinPermisos, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostForm
    template_name_suffix = '_update_form'
    success_message = "Post actualizado satisfactoriamente"
    success_url = reverse_lazy('blog_dash:list')

    # filtra el el queryset por autor, solo podra editar los post que sean de su propiedad
    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostDeleteView(SinPermisos, DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
    success_url = reverse_lazy('blog_dash:list')
    success_message = "Post eliminado satisfactoriamente"

    # Toca meterle esto devido a un error en django, para que mande el mensaje
    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.imagen.delete()
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)


############################### COMENTARIOS #######################
# class ComentarioCreateView(CreateView):
#     model = Comentario
#     form_class = ComentarioForm
#     success_message = "Comentario creado satisfactoriamente"
#     success_url = reverse_lazy('detallepost')

#     def dispatch(self, request, *args, **kwargs):
#         self.post = get_object_or_404(Post, pk=kwargs['post_id'])
#         return super().dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         form.instance.post = self.post
#         return super().form_valid(form)
    
#     def get_success_url(self):
#         return reverse_lazy('detallepost', args=[self.post.slug]) + '?ok'