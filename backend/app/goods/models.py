from django.db import models
import uuid
from app.products.models import Product

class Bag(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    height = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    width = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    length = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    depth = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    pockets = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    main_compartment = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    top_opening = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="bags"
    )
    class Meta:
        db_table = "bags"
        verbose_name = "Bag"
        verbose_name_plural = "Bags"
    
    def __str__(self):
        return f"{self.name}"

class Glove(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    height = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    length = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    opening_size = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="gloves"
    )
    class Meta:
        db_table = "gloves"
        verbose_name = "Glove"
        verbose_name_plural = "Gloves"
    
    def __str__(self):
        return f"{self.name}"

class Airgear(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    length = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    height = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    width = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    depth = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    number_of_pumps = models.PositiveSmallIntegerField(
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="airgear"
    )
    class Meta:
        db_table = "airgear"
        verbose_name = "Airgear"
        verbose_name_plural = "Airgear"
        ordering = ["-height"]
    
    def __str__(self):
        return f"{self.name}"

class Attribute(models.Model):
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
        db_table = "attributes"
        verbose_name = "Attribute"
        verbose_name_plural = "Attributes"
        ordering = ["-name"]
    
    def __str__(self):
        return self.name

class Oil(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    volume = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    attributes = models.ForeignKey(
        Attribute, on_delete=models.PROTECT,
        related_name="oil"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="oil"
    )
    class Meta:
        db_table = "oil"
        verbose_name = "Oil"
        verbose_name_plural = "Oil"
    
    def __str__(self):
        return self.name

class Trophy(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    height = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    release_date = models.DateField(
        blank=True,
        null=True
    )
    expiration_date = models.DateField(
        blank=True,
        null=True
    )
    scale = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="trophy"
    )
    
    class Meta:
        db_table = "trophy"
        verbose_name = "Trophy"
        verbose_name_plural = "Trophies"
    
    def __str__(self):
        return self.name