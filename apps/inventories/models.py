from django.db import models

from apps.branches.models import Branch
from apps.default.models import BaseModel


class Inventory(BaseModel):
    batch = models.CharField(max_length=150, default="", null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=True)
    description = models.CharField(max_length=500, default="", null=True, blank=True)

    class Meta:
        abstract = True


class RawMaterialsInventory(Inventory):
    expiration = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class EquipmentsInventory(Inventory):
    is_working = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.name}"
