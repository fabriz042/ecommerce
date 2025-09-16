from django.contrib import admin
from .models import Product, Character, Status, Brand, Category, Series, Tag, Sport

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'weight', 'short_description', 'slug', 'status', 'brand', 'category', 'series', 'character')
    list_filter = ('status', 'status__name', 'brand', 'category', 'series', 'character')
    search_fields = ('name',)

    def short_description(self, obj):
        if obj.description:
            return f"{obj.description[:10]}..." if len(obj.description) > 10 else obj.description
        return "--"
    short_description.short_description = "Description"

class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Sport, SportAdmin)
