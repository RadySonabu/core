from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class AddressBaseModel(BaseModel):
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    barangay = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)

    class Meta:
        abstract = True
