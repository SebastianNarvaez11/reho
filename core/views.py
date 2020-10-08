from django.shortcuts import render, redirect
from .models import Business
from .forms import BusinessForm
from services.models import Service
from trabajos.models import Trabajo
from blog.models import Post
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from dash.views import SinPermisos
from django.urls import reverse_lazy
from django.contrib import messages
from contact.forms import SuscribeForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.


def index(request):
    if not Business.objects.all():
        Business.objects.create(nombre='nombreempresa', lema='lemaempresa', logo='null',
                                email='email@gmail.com', direccion='direccionempresa', telefonos='123456', wpp='31231',
                                horarios='horariosbusiness', descripcion='', mision='', vision='',
                                historia='', creacion='', edicion='')
        return redirect('business_urldash:create', pk=1)

    posts = Post.objects.all()
    trabajos = Trabajo.objects.filter(index=True)

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
                return redirect(reverse('index')+"?ok")
            except:
                return redirect(reverse('index')+"?fail")

    return render(request, 'core/index.html', {'lista_posts': posts, 'lista_trabajos': trabajos, 'formulario': suscribe_form})


def about(request):
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
                return redirect(reverse('about')+"?ok")
            except:
                return redirect(reverse('about')+"?fail")

    return render(request, 'core/about.html', {'formulario': suscribe_form})

####################################### Vistas del Dashboard #############################################

# Vista para actualizar la informacion del business
@method_decorator(login_required, name='dispatch')
class BusinessUpdateView(SinPermisos, UpdateView):
    permission_required = 'core.change_business'
    model = Business
    form_class = BusinessForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('home')
    success_message = 'Datos actualizados satisfactoriamente'

# vista para crear/actualizar el business,(ya que se crea un objeto business por defecto) en caso de que no exista
# la vista simula la creacion del business
@method_decorator(login_required, name='dispatch')
class BusinessUpdateCreate(SinPermisos, UpdateView):
    model = Business
    form_class = BusinessForm
    success_url = reverse_lazy('home')
    template_name = 'core/business_form.html'
    success_message = 'Datos creados satisfactoriamente'
