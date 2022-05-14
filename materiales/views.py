from django.shortcuts import render, get_object_or_404, redirect
from .models import Material
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import MaterialForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.contrib import messages
from contact.forms import SuscribeForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def materiales(request):
    pinturas = Material.objects.filter(categoria=3)
    telas = Material.objects.filter(categoria=1)
    maderas = Material.objects.filter(categoria=2)

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

    return render(request, 'materiales/materiales.html', {'telas': telas, 'maderas': maderas, 'pinturas': pinturas, 'formulario': suscribe_form})


def detallematerial(request, slug_material):
    material = get_object_or_404(Material, slug=slug_material)

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

    return render(request, 'materiales/detallematerial.html', {'material': material, 'formulario': suscribe_form})


def prana(request):

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

    return render(request, 'materiales/prana.html', {'formulario': suscribe_form})


def cuerotext(request):

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

    return render(request, 'materiales/cuerotext.html', {'formulario': suscribe_form})


def bisont(request):

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

    return render(request, 'materiales/bisont.html', {'formulario': suscribe_form})


def capadocia(request):

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

    return render(request, 'materiales/capadocia.html', {'formulario': suscribe_form})


def acqua(request):

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

    return render(request, 'materiales/acqua.html', {'formulario': suscribe_form})


def betel(request):

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

    return render(request, 'materiales/betel.html', {'formulario': suscribe_form})


def dominio(request):

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

    return render(request, 'materiales/dominio.html', {'formulario': suscribe_form})


def bizantino(request):

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

    return render(request, 'materiales/bizantino.html', {'formulario': suscribe_form})


def berbera(request):

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

    return render(request, 'materiales/berbera.html', {'formulario': suscribe_form})


def agata(request):

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

    return render(request, 'materiales/agata.html', {'formulario': suscribe_form})

def bruselas(request):

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

    return render(request, 'materiales/bruselas.html', {'formulario': suscribe_form})


def belgica(request):

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

    return render(request, 'materiales/belgica.html', {'formulario': suscribe_form}) 


def durazno(request):

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

    return render(request, 'materiales/durazno.html', {'formulario': suscribe_form}) 

def natura(request):

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

    return render(request, 'materiales/natura.html', {'formulario': suscribe_form}) 


def palermo(request):

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

    return render(request, 'materiales/palermo.html', {'formulario': suscribe_form}) 


def marmol(request):

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

    return render(request, 'materiales/marmol.html', {'formulario': suscribe_form}) 



def asturias(request):

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

    return render(request, 'materiales/asturias.html', {'formulario': suscribe_form}) 
#--------------------Vistas Del Dashboard-----------------------#


@method_decorator(login_required, name='dispatch')
class MaterialListView(SinPermisos, ListView):
    permission_required = 'materiales.view_material'
    model = Material


@method_decorator(login_required, name='dispatch')
class MaterialCreateView(SinPermisos, CreateView):
    permission_required = 'materiales.add_Material'
    model = Material
    form_class = MaterialForm
    success_url = reverse_lazy('materiales_dash:list')
    success_message = 'Material creado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class MaterialUpdateView(SinPermisos, UpdateView):
    permission_required = 'materiales.change_material'
    model = Material
    form_class = MaterialForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('materiales_dash:list')
    success_message = 'Material actualizado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class MaterialDeleteView(SinPermisos, DeleteView):
    permission_required = 'materiales.delete_material'
    model = Material
    success_url = reverse_lazy('materiales_dash:list')
    success_message = 'Material eliminado satisfactoriamente'

    # Toca meterle esto devido a un error en django para que envie el mensaje
    def delete(self, request, *args, **kwargs):
        Material = self.get_object()
        Material.imagen1.delete()
        Material.imagen2.delete()
        messages.success(self.request, self.success_message)
        return super(MaterialDeleteView, self).delete(request, *args, **kwargs)
