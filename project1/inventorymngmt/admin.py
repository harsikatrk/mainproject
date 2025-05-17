from django.contrib import admin
from .models import Inventory

# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'availableQtyGrams','availableQtyPieces','pricePerGram','pricePerPiece')
    search_fields = ['name', 'category']

admin.site.register(Inventory, InventoryAdmin)
# Register your models here.
