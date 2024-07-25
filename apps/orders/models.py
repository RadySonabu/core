from django.db import models
from ..items.models import Item
from django.db.models.signals import pre_save
from django.dispatch import receiver


class OrderNumberField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("max_length", 8)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("editable", False)
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        if not value:
            # Generate the new order number
            last_order = model_instance.__class__.objects.last()
            last_order_number = int(last_order.order_number[3:]) if last_order else 0
            value = f"OID{last_order_number + 1:05}"
        return value


class OrderStatus(models.TextChoices):
    PENDING = "P", ("Pending")
    DONE = "D", ("Done")
    CANCELLED = "C", ("Cancelled")


class OrderConsumption(models.TextChoices):
    DINE_IN = "D", ("Dine-In")
    TAKE_OUT = "T", ("Take-Out")


class Order(models.Model):
    order_number = OrderNumberField()
    mode_of_consumption = models.CharField(
        max_length=20,
        choices=OrderConsumption.choices,
        default=OrderConsumption.DINE_IN,
    )
    status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING
    )
    is_paid = models.BooleanField(default=False)
    note = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return f"{self.order_number} - {self.is_paid}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    description = models.CharField(max_length=150, blank=True)

    def __str__(self) -> str:
        return f"{self.order.order_number} - {self.order.is_paid} - {self.item.name} x{self.quantity}"
