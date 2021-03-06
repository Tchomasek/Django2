from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True)
    summary = models.TextField(blank=True)
    featured = models.BooleanField(default=True)
