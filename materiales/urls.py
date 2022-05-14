from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', views.materiales, name='materiales'),
    path('<slug:slug_material>/', views.detallematerial, name='detallematerial'),
    path('telas/prana/', views.prana, name='prana'),
    path('telas/cuerotext/', views.cuerotext, name='cuerotext'),
    path('telas/bisont/', views.bisont, name='bisont'),
    path('telas/capadocia/', views.capadocia, name='capadocia'),
    path('telas/acqua/', views.acqua, name='acqua'),
    path('telas/betel/', views.betel, name='betel'),
    path('telas/dominio/', views.dominio, name='dominio'),
    path('telas/bizantino/', views.bizantino, name='bizantino'),
    path('telas/berbera/', views.berbera, name='berbera'),
    path('telas/agata/', views.agata, name='agata'),
    path('telas/bruselas/', views.bruselas, name='bruselas'),
    path('telas/belgica/', views.belgica, name='belgica'),
    path('telas/durazno/', views.durazno, name='durazno'),
    path('telas/natura/', views.natura, name='natura'),
    path('telas/palermo/', views.palermo, name='palermo'),
    path('telas/marmol/', views.marmol, name='marmol'),
    path('telas/asturias/', views.asturias, name='asturias')
]

materiales_urldash = ([
    path('list/', MaterialListView.as_view(), name='list'),
    path('create/', MaterialCreateView.as_view(), name='create'),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete')
], 'materiales_dash')
