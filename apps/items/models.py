from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField(default=0.00)
    description = models.CharField(max_length=150, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
