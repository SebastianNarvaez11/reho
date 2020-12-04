from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProductoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from dash.views import SinPermisos
from django.utils.decorators import method_decorator
from django.contrib import messages
from contact.forms import SuscribeForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.


def productos(request):
    nuevos = Producto.objects.filter(categoria=1)
    restaurados = Producto.objects.filter(categoria=2)

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
                return redirect(reverse('productos')+"?ok")
            except:
                return redirect(reverse('productos')+"?fail")

    return render(request, 'productos/productos.html', {'nuevos': nuevos, 'restaurados' : restaurados, 'formulario': suscribe_form})


def detalleproducto(request, slug_producto):
    producto = get_object_or_404(Producto, slug=slug_producto)

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
                return redirect(reverse('productos')+"?ok")
            except:
                return redirect(reverse('productos')+"?fail")

    return render(request, 'productos/detalleproducto.html', {'producto': producto, 'formulario': suscribe_form})

#--------------------Vistas Del Dashboard-----------------------#


@method_decorator(login_required, name='dispatch')
class ProductoListView(SinPermisos, ListView):
    permission_required = 'productos.view_producto'
    model = Producto


@method_decorator(login_required, name='dispatch')
class ProductoCreateView(SinPermisos, CreateView):
    permission_required = 'productos.add_Producto'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('productos_dash:list')
    success_message = 'Producto creado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class ProductoUpdateView(SinPermisos, UpdateView):
    permission_required = 'productos.change_producto'
    model = Producto
    form_class = ProductoForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('productos_dash:list')
    success_message = 'Producto actualizado satisfactoriamente'


@method_decorator(login_required, name='dispatch')
class ProductoDeleteView(SinPermisos, DeleteView):
    permission_required = 'productos.delete_producto'
    model = Producto
    success_url = reverse_lazy('productos_dash:list')
    success_message = 'Producto eliminado satisfactoriamente'

    # Toca meterle esto devido a un error en django para que envie el mensaje
    def delete(self, request, *args, **kwargs):
        Producto = self.get_object()
        Producto.imagen1.delete()
        Producto.imagen2.delete()
        Producto.imagen3.delete()
        Producto.imagen4.delete()
        messages.success(self.request, self.success_message)
        return super(ProductoDeleteView, self).delete(request, *args, **kwargs)
