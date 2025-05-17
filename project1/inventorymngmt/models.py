from django.db import models
class Inventory(models.Model):
    category = models.CharField(max_length=15,null=False, blank="False")
    name = models.CharField(max_length=30,null=False, blank="False")
    pricePerGram = models.FloatField(null=True, blank=False)
    pricePerPiece = models.FloatField(null=True, blank=False)
    availableQtyGrams = models.FloatField(null=True, blank=False)
    availableQtyPieces = models.IntegerField(null=True, blank=False)

    class Meta:
        verbose_name_plural = "Inventory"

# Create your models here.
