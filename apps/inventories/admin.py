from django.contrib import admin

from apps.inventories.models import InventoryCategory, InventoryItem


class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "purchase_price", "updated_at")
    ordering = ("-updated_at",)
    list_filter = ("category", "name", "status", "updated_at")
    search_fields = ("name", "description")


admin.site.register(InventoryCategory)
admin.site.register(InventoryItem, InventoryItemAdmin)
