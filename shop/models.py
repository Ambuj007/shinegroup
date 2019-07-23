from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.


class Stock(models.Model):
    category            = models.CharField(max_length=120)
    brand               = models.CharField(max_length=120)
    item                = models.CharField(max_length=120, blank=True)
    item_type           = models.CharField(max_length=120)
    item_specification  = models.CharField(max_length=120)
    model_no            = models.CharField(max_length=120, blank=True)
    purchase_price      = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price       = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category


class Notice(models.Model):
    notice = models.CharField(max_length=120)


class Demand(models.Model):
    item     = models.CharField(max_length=120)
    quantity = models.IntegerField(default='0')
    date_created = models.DateTimeField(default=timezone.now)
