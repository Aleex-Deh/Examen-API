from django.urls import path
from . import views

# Aquí le asigno una URL a mis funciones dentro del views (.views)

urlpatterns = [
    path('list-socio/', views.list_socios, name='list_socios'),
    path('add-socio/', views.add_socio, name='add_socio'),
    path('edit-password/', views.edit_password, name='edit_password'),



]