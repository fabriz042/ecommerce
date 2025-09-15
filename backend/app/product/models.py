from django.db import models
import uuid
from django.utils.text import slugify

class Status(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255
    )
    
    class Meta:
        db_table = "status"
        verbose_name = "Status"
        verbose_name_plural = "Status"
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255
    )
    
    class Meta:
        db_table = "brands"
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255
    )
    
    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name

class Series(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255
    )
    
    class Meta:
        db_table = "series"
        verbose_name = "Series"
        verbose_name_plural = "Series"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name

class Character(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255
    )
    
    class Meta:
        db_table = "characters"
        verbose_name = "Character"
        verbose_name_plural = "Characters"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255
    )
    stock = models.PositiveSmallIntegerField(
        default=0
    )
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2
    )
    weight = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        blank=True,
        null=True
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    slug = models.SlugField(
        max_length=255, 
        unique=True,
        blank=True,
        null=True
    )
    status = models.ForeignKey(
        Status, on_delete=models.PROTECT,
        related_name="products"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT,
        related_name="products"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        related_name="products"
    )
    series = models.ForeignKey(
        Series, on_delete=models.PROTECT,
        related_name="products",
        blank=True,
        null=True
    )
    character = models.ForeignKey(
        Character, on_delete=models.PROTECT,
        related_name="products",
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-price"]
    
    def __str__(self):
        return self.name

