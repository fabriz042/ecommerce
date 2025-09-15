import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
    
class Role(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    name = models.CharField(
        max_length=255,
        unique=True
    )
    
    class Meta:
        db_table = 'roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class User(AbstractUser):
    DOCUMENT_TYPES = [
        ("PASS", "Passport"),
        ("NID", "National ID"),
        ("SSN", "Social Security Number"),
        ("TAX", "Tax ID / VAT"),
        ("DRIV", "Driver License"),
    ]
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )
    username = models.CharField(
        max_length=30,
        blank=False,
        unique=True,
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    email = models.EmailField(
        max_length=100,
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
    )
    document_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    document_type = models.CharField(
        max_length=10,
        choices=DOCUMENT_TYPES,
        blank=True,
        null=True,
    )
    join_date = models.DateTimeField(
        auto_now_add=True,
    )
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-join_date']
    
    def __str__(self):
        return self.username