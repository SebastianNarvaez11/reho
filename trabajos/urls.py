from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.trabajos, name='trabajos'),
    path('<slug:slug_trabajo>/', views.detalletrabajo, name='detalletrabajo'),
]

trabajos_urldash = ([
    path('list/', TrabajoListView.as_view(), name='list'),
    path('create/', TrabajoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TrabajoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrabajoDeleteView.as_view(), name='delete')
], 'trabajos_dash')
