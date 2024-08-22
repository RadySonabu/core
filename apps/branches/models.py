from django.db import models

from apps.default.models import AddressBaseModel


class Branch(AddressBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(default="", null=True, blank=True)

    def __str__(self) -> str:
        return f"Branch: {self.name} | {self.city}, {self.street}"

    class Meta:
        verbose_name_plural = "branches"
