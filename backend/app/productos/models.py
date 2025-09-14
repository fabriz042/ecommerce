from django.db import models
    
class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = "estado"  # Nombre exacto de la tabla en MySQL
    
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    images = models.PositiveSmallIntegerField() 
    
    class Meta:
        db_table = 'productos'  # <-- Aquí le dices a Django que use la tabla "productos"
