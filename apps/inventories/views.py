from django.shortcuts import render

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.inventories.api import InventoryCategorySerializer, InventoryItemSerializer
from apps.inventories.models import InventoryCategory, InventoryItem


# Create your views here.
class InventoryItemViewset(ModelViewSet):
    model = InventoryItem
    serializer_class = InventoryItemSerializer
    queryset = InventoryItem.objects.all()
