from typing import Any
from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet

from apps.inventories.api import InventoryCategorySerializer, InventoryItemSerializer
from apps.inventories.forms import InventoryItemForm
from apps.inventories.models import InventoryCategory, InventoryItem

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
import django_tables2 as tables

from apps.inventories.table import InventoryItemTable
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django_filters import FilterSet, CharFilter
from django.db.models import Q


# Create your views here.
class InventoryItemViewset(ModelViewSet):
    model = InventoryItem
    serializer_class = InventoryItemSerializer
    queryset = InventoryItem.objects.all()


class InventoryItemFilter(FilterSet):
    search = CharFilter(method="filter_by_search_term", label="Search")

    class Meta:
        model = InventoryItem
        fields = []

    def filter_by_search_term(self, queryset, name, value):
        # Use Q objects to combine the conditions
        query = (
            Q(name__icontains=value)
            | Q(description__icontains=value)
            | Q(status__icontains=value)
            | Q(category__name__icontains=value)
        )
        return queryset.filter(query)


class InventoryListView(tables.SingleTableMixin, FilterView):
    table_class = InventoryItemTable
    model = InventoryItem
    template_name = "inventories/inventoryitem_list.html"
    filterset_class = InventoryItemFilter


class InventoryCreateView(CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    success_url = reverse_lazy("inventory_item_list")
