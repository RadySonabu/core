from rest_framework import serializers

from apps.inventories.models import InventoryItem, InventoryCategory


class InventoryItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryItem
        fields = "__all__"


class InventoryCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = InventoryCategory
        fields = "__all__"
