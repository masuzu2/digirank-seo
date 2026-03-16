from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact/', views.contact),           # ข้อ 1
    path('form/', views.form, name='form'),    # ข้อ 2
]