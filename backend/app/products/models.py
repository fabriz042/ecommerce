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
    included = models.CharField(
        max_length=255,
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

def img_path_products(instance, filename):
    return f"products/{instance.product.id}/{filename}"

class ProductImage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image_url = models.ImageField(
        upload_to=img_path_products,
    )
    alt_text = models.CharField(
        max_length=255,
        blank=True,
        null=False,
    )
    order = models.PositiveSmallIntegerField(
        default=0,
    )
    is_main = models.BooleanField(
        default=False,
    )

    def save(self, *args, **kwargs):
        if not self.alt_text and self.product_id:
            self.alt_text = f"Image from {self.product.name}"[:255]
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = "product_images"
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["product", "order"],
                name="unique_product_image_order"
            ),
            models.UniqueConstraint(
                fields=["product"],
                condition=models.Q(is_main=True),
                name="unique_main_image_per_product"
            ),
        ]

    def __str__(self):
        return f"{self.product.name} - \"image n°{self.order}\""
    
class Tag(models.Model):
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
    products = models.ManyToManyField(
        Product,
        related_name="tags"
    )
    
    class Meta:
        db_table = "tags"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name

class Sport(models.Model):
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
    products = models.ManyToManyField(
        Product,
        related_name="sports"
    )

    class Meta:
        db_table = "sports"
        verbose_name = "Sport"
        verbose_name_plural = "Sports"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name
