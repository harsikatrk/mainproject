from django.contrib import admin
from .models import Billing

# Register your models here.

class BillingAdmin(admin.ModelAdmin):
    list_display = ('billno','name','mobile','address','area','city','pincode','order_date','delivery_date','sweets','sweet_pieces','savouries','savouries_gram','paymenttype','amount','advance','packaging_detail')
    search_fields = ['billno','name','mobile','address','area','city','pincode','order_date','delivery_date','sweets','sweet_pieces','savouries','savouries_gram','paymenttype','amount','advance','packaging_detail']

admin.site.register(Billing, BillingAdmin)
# Register your models here.



