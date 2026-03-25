from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('clients/', views.clients, name='clients'),
    path('clients/add/', views.client_add, name='client_add'),
    path('clients/edit/<int:id>/', views.client_edit, name='client_edit'),
    path('clients/delete/<int:id>/', views.client_delete, name='client_delete'),
    path('clients/search/', views.client_search, name='client_search'),
    path('contact/', views.contact, name='contact'),
]
