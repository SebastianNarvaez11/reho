from django.urls import path
from .import views
from .views import BusinessUpdateCreate, BusinessUpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('about/', views.about, name='about'),
]

business_urldash = ([
    path('create/<int:pk>/', BusinessUpdateCreate.as_view(), name='create'),
    path('update/<int:pk>/', BusinessUpdateView.as_view(), name='update'),
], 'business_urldash')
