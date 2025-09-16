from django.contrib import admin

from .models import Bag, Airgear, Oil, Trophy, Glove

class BagAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'width', 'length', 'depth', 'pockets', 'main_compartment', 'top_opening', 'accessories_included')
    list_filter = ('height', 'width', 'length', 'depth', 'pockets', 'main_compartment', 'top_opening', 'accessories_included')
    search_fields = ('name',)

admin.site.register(Bag)
admin.site.register(Glove)
admin.site.register(Airgear)
admin.site.register(Oil)
admin.site.register(Trophy)

