from django.contrib import admin
from .models import Customer # Calling another python file or module

# Register your models here.

# admin.site.register(Customer) # Register the required models to be visible in the admin panel.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id","name","mobile","address","area","city", "pincode")
    search_fields = ["name","mobile","address","area","city", "pincode"]
admin.site.register(Customer, CustomerAdmin)

# Register your models here.
