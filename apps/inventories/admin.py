from django.contrib import admin

from apps.inventories.models import RawMaterialsInventory, EquipmentsInventory

admin.site.register(RawMaterialsInventory)
admin.site.register(EquipmentsInventory)
