from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role
from django.contrib.auth.models import Group

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'role', 'is_staff', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'document_number', 'document_type', 'is_active', 'join_date')
    list_filter = ('is_staff', 'is_active', 'role')
    search_fields = ('username', 'email')
    ordering = ('-join_date',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('email', 'first_name', 'last_name', 'phone_number', 'document_number', 'document_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
        ('Dates', {'fields': ('last_login', 'join_date')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active', 'role', 'first_name', 'last_name', 'phone_number', 'document_number', 'document_type'),
        }),
    )
    
    readonly_fields = ('last_login', 'join_date')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('-name',)

admin.site.register(Role, RoleAdmin)
admin.site.unregister(Group)