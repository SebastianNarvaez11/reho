from django.shortcuts import render, get_object_or_404, redirect
from .models import Trabajo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import TrabajoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.contrib import messages
from contact.forms import SuscribeForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def trabajos(request):
    trabajos_restauracion = Trabajo.objects.filter(categoria=3)
    trabajos_retapizados = Trabajo.objects.filter(categoria=1)
    trabajos_fabricados = Trabajo.objects.filter(categoria=2)

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
                return redirect(reverse('trabajos')+"?ok")
            except:
                return redirect(reverse('trabajos')+"?fail")

    return render(request, 'trabajos/trabajos.html', {'restaurados': trabajos_restauracion, 'retapizados' : trabajos_retapizados, 'fabricados' : trabajos_fabricados, 'formulario': suscribe_form})


def detalletrabajo(request, slug_trabajo):
    trabajo = get_object_or_404(Trabajo, slug=slug_trabajo)

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
                return redirect(reverse('materiales')+"?ok")
            except:
                return redirect(reverse('materiales')+"?fail")

    return render(request, 'trabajos/detalletrabajo.html', {'trabajo': trabajo, 'formulario': suscribe_form})

#--------------------Vistas Del Dashboard-----------------------#


@method_decorator(login_required, name='dispatch')
class TrabajoListView(SinPermisos, ListView):
    permission_required = 'trabajos.view_trabajo'
    model = Trabajo


@method_decorator(login_required, name='dispatch')
class TrabajoCreateView(SinPermisos, CreateView):
    permission_required = 'trabajos.add_Trabajo'
    model = Trabajo
    form_class = TrabajoForm
    success_url = reverse_lazy('trabajos_dash:list')
    success_message = 'Trabajo creado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class TrabajoUpdateView(SinPermisos, UpdateView):
    permission_required = 'trabajos.change_trabajo'
    model = Trabajo
    form_class = TrabajoForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('trabajos_dash:list')
    success_message = 'Trabajo actualizado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class TrabajoDeleteView(SinPermisos, DeleteView):
    permission_required = 'trabajos.delete_trabajo'
    model = Trabajo
    success_url = reverse_lazy('trabajos_dash:list')
    success_message = 'Trabajo eliminado satisfactoriamente'

    # Toca meterle esto devido a un error en django para que envie el mensaje
    def delete(self, request, *args, **kwargs):
        Trabajo = self.get_object()
        Trabajo.imagen1.delete()
        Trabajo.imagen2.delete()
        messages.success(self.request, self.success_message)
        return super(TrabajoDeleteView, self).delete(request, *args, **kwargs)
