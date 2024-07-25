from django.urls import path
from . import views

urlpatterns = [
    # path("", views.orders_page),
    path("", views.OrderListView.as_view(), name="order_list"),
    path("add/", views.OrderCreateView.as_view(), name="order_create"),
]
