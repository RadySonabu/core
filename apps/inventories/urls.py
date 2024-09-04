from django.urls import path
from . import views

urlpatterns = [
    # path("", views.orders_page),
    path("inventory/", views.InventoryListView.as_view(), name="inventory_item_list"),
    # path("pending/", views.PendingOrderListView.as_view(), name="pending_order_list"),
    # path("done/", views.DoneOrderListView.as_view(), name="done_order_list"),
    path(
        "inventory/add/", views.InventoryCreateView.as_view(), name="inventory_create"
    ),
    # path("items/<int:pk>/", views.OrderItemListView.as_view(), name="orderitem_list"),
    # path("items/add/", views.OrderItemCreateView.as_view(), name="orderitem_create"),
]
