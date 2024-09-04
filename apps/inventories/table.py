import django_tables2 as tables

from apps.inventories.models import InventoryItem


class InventoryItemTable(tables.Table):

    category = tables.Column(accessor="category__name", verbose_name="Category")
    quantity = tables.Column(empty_values=(), verbose_name="Quantity")

    class Meta:
        model = InventoryItem
        fields = (
            "category",
            "name",
            "quantity",
            "status",
            "packaging",
        )

    def render_quantity(self, record):
        # Combine first_name and last_name to create full_name
        return f"{record.quantity} {record.measurement}"
