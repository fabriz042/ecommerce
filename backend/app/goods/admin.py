from django.contrib import admin

from .models import Bag, Airgear, Oil, Trophy, Glove, Attribute

class BagAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'width', 'length', 'depth', 'pockets', 'main_compartment', 'top_opening', 'accessories_included')
    list_filter = ('height', 'width', 'length', 'depth', 'pockets', 'main_compartment', 'top_opening', 'accessories_included')
    search_fields = ('name',)

class GloveAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'length', 'opening_size')
    list_filter = ('height', 'length', 'opening_size')
    search_fields = ('name',)

class AirgearAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'length', 'width')
    list_filter = ('height', 'length', 'width')
    search_fields = ('name',)

class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class OilAdmin(admin.ModelAdmin):
    list_display = ('name', 'volume')
    list_filter = ('volume',)
    search_fields = ('name',)

class TrophyAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'length', 'width')
    list_filter = ('height', 'length', 'width')
    search_fields = ('name',)

admin.site.register(Bag)
admin.site.register(Glove)
admin.site.register(Airgear)
admin.site.register(Attribute)
admin.site.register(Oil)
admin.site.register(Trophy)

