from django.contrib import admin

# Register your models here.
from .models import Producto

admin.site.register(Producto)  # Registra el modelo en el admin