from django.contrib import admin
from.models import items
# Register your models here.
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'image')
admin.site.register(items,ItemsAdmin)

