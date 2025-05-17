from django.db import models

class Billing(models.Model): # Table Name
    # Following are the Columns of a Table
    billno=models.IntegerField(null=False,blank=False)
    name = models.CharField(max_length=30,null=False,blank=False)
    mobile = models.IntegerField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=50,null=False,blank=False)
    area = models.CharField(max_length=20,null=False,blank=False)
    city = models.CharField(max_length=20,null=False,blank=False)
    pincode = models.IntegerField(null=False, blank=False)
    order_date=models.IntegerField(null=False,blank=False)
    delivery_date=models.IntegerField(null=False,blank=False)
    sweets=models.CharField(max_length=50,null=False,blank=False)
    sweet_pieces=models.IntegerField(null=False,blank=False)
    savouries=models.CharField(max_length=50,null=False,blank=False)
    savouries_gram=models.IntegerField(null=False,blank=False)
    paymenttype=models.CharField(max_length=20,null=False,blank=False)
    amount=models.IntegerField(null=False,blank=False)
    advance=models.IntegerField(null=False,blank=False)
    packaging_detail=models.CharField(max_length=50,null=False,blank=False)


    def __str__(self):
        return self.name


# Create your models here.
