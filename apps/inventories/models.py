from django.db import models

from apps.branches.models import Branch
from apps.default.models import BaseModel


IN_STOCK = "in_stock"
OUT_OF_STOCK = "out_of_stock"
DISCONTINUED = "discontinued"
ITEM_STATUS_CHOICES = [
    ("in_stock", "In Stock"),
    ("out_of_stock", "Out of Stock"),
    ("discontinued", "Discontinued"),
]


KG = "kilograms"
L = "liters"
GAL = "gallons"

MEASUREMENT_CHOICES = [
    (KG, "Kilograms"),
    (L, "Liters"),
    (GAL, "Gallons"),
]


class InventoryCategory(BaseModel):
    name = models.CharField(max_length=150, null=True)
    description = models.CharField(
        max_length=500, default="No description provided.", null=True, blank=True
    )

    def __str__(self):
        return f"{self.name} | {self.description}"

    class Meta:
        verbose_name_plural = "inventory categories"


class InventoryItem(BaseModel):
    """Inventory Item class

    Example:
    storage = HQ
    category = Raw Material
    name = chicken breast
    description = chicken breast fillet that is frozen
    measurement = kg
    quantity = 20
    purchase_price = 4000
    status = in_stock

    """

    storage = models.ForeignKey(Branch, on_delete=models.CASCADE)
    category = models.ForeignKey(
        InventoryCategory, on_delete=models.CASCADE, related_name="inventory_items"
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    measurement = models.CharField(max_length=50, choices=MEASUREMENT_CHOICES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=15, choices=ITEM_STATUS_CHOICES, default=IN_STOCK
    )

    def __str__(self) -> str:
        return f"{self.storage.name} | {self.category.name} | {self.name} | x{self.quantity} {self.measurement}"

    @property
    def is_in_stock(self):
        return self.quantity > 0
