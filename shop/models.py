from django.db import models

# Create your models here.


class Stock(models.Model):
    category        = models.CharField(max_length=120)
    brand           = models.CharField(max_length=120)
    item            = models.CharField(max_length=120, blank=True)
    typep            = models.CharField(max_length=120)
    specificationp   = models.CharField(max_length=120)
    Model_No        = models.CharField(max_length=120, blank=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price   = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category


class Notice(models.Model):
    Notice        = models.CharField(max_length=120)


class DemandModel(models.Model):
    Item        = models.CharField(max_length=120)
    Quantity    = models.IntegerField(default='0') 


