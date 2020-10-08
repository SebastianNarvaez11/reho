from django.urls import path
from .import views
from .views import PostListView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<slug:slug_post>/', views.detallepost, name='detallepost')
]

blog_urldash = ([
    path('list/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),
], 'blog_dash')