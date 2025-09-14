from django.urls import path
from .views import buscar_productos
from .views import slug_productos

urlpatterns = [
    path('busqueda/', buscar_productos),
    path('productos/<slug:slug>/', slug_productos), 
    
]
