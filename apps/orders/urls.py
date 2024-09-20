from django.urls import path
from . import views

urlpatterns = [
    path("", views.PendingOrDone.as_view(), name="pending_or_done_orders"),
    path("pending/", views.PendingOrderListView.as_view(), name="pending_order_list"),
    path("done/", views.DoneOrderListView.as_view(), name="done_order_list"),
    path("add/", views.OrderCreateView.as_view(), name="order_create"),
    path("items/<int:pk>/", views.OrderItemListView.as_view(), name="orderitem_list"),
    path("items/add/", views.OrderItemCreateView.as_view(), name="orderitem_create"),
]
