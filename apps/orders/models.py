from django.db import models
from ..items.models import Item


class Order(models.Model):
    order_number = models.CharField(max_length=20)
    is_paid = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.order_number} - {self.is_paid}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.order.order_number} - {self.order.is_paid} - {self.item.name}"
