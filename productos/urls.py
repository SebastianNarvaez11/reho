from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.productos, name='productos'),
    path('<slug:slug_producto>/', views.detalleproducto, name='detalleproducto'),
]

productos_urldash = ([
    path('list/', ProductoListView.as_view(), name='list'),
    path('create/',ProductoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductoDeleteView.as_view(), name='delete')
], 'productos_dash')
