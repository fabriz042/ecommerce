from django.contrib import admin
from .models import Product, ProductImage , Character, State, Brand, Category, Series, Tag, Sport

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fk_name = "product"
    extra = 1

class ProductTagInline(admin.TabularInline):
    model = Tag.products.through
    extra = 1

class ProductSportInline(admin.TabularInline):
    model = Sport.products.through
    extra = 1
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price', 'weight', 'short_description', 'slug', 'state', 'brand', 'category', 'series', 'character', 'included')
    list_filter = ('state', 'brand', 'category', 'series', 'character')
    search_fields = ('name',)
    inlines = [ProductImageInline, ProductTagInline, ProductSportInline]

    def short_description(self, obj):
        if obj.description:
            return f"{obj.description[:10]}..." if len(obj.description) > 10 else obj.description
        return "--"
    short_description.short_description = "Description"

class StateAdmin(admin.ModelAdmin):
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
admin.site.register(State, StateAdmin)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Sport, SportAdmin)
