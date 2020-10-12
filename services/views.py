from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ServiceForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.contrib import messages
from contact.forms import SuscribeForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def services(request):
    servicios = Service.objects.filter(estado=True)
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
                return redirect(reverse('services')+"?ok")
            except:
                return redirect(reverse('services')+"?fail")

    return render(request, 'services/services.html', {'lista_servicios': servicios, 'formulario': suscribe_form})


def detalleservicio(request, slug_servicio):
    service = get_object_or_404(Service, slug=slug_servicio)

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
                return redirect(reverse('services')+"?ok")
            except:
                return redirect(reverse('services')+"?fail")
                
    return render(request, 'services/detalleservicio.html', {'servicio': service, 'formulario': suscribe_form})

#--------------------Vistas Del Dashboard-----------------------#


@method_decorator(login_required, name='dispatch')
class ServiceListView(SinPermisos, ListView):
    permission_required = 'services.view_service'
    model = Service


@method_decorator(login_required, name='dispatch')
class ServiceCreateView(SinPermisos, CreateView):
    permission_required = 'services.add_service'
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services_dash:list')
    success_message = 'Servicio creado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class ServiceUpdateView(SinPermisos, UpdateView):
    permission_required = 'services.change_service'
    model = Service
    form_class = ServiceForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('services_dash:list')
    success_message = 'Servicio actualizado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class ServiceDeleteView(SinPermisos, DeleteView):
    permission_required = 'services.delete_service'
    model = Service
    success_url = reverse_lazy('services_dash:list')
    success_message = 'Servicio eliminado satisfactoriamente'

    # Toca meterle esto devido a un error en django para que envie el mensaje
    def delete(self, request, *args, **kwargs):
        service = self.get_object()
        service.imagen1.delete()
        service.imagen2.delete()
        messages.success(self.request, self.success_message)
        return super(ServiceDeleteView, self).delete(request, *args, **kwargs)
