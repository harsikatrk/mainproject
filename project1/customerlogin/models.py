from django.db import models

class Customer(models.Model): # Table Name
    # Following are the Columns of a Table
    name = models.CharField(max_length=30,null=False,blank=False)
    mobile = models.IntegerField(null=False, blank=False, unique=True)
    address = models.CharField(max_length=50,null=False,blank=False)
    area = models.CharField(max_length=20,null=False,blank=False)
    city = models.CharField(max_length=20,null=False,blank=False)
    pincode = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

# Create your models here.
