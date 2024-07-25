from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from apps.orders.forms import OrderForm, OrderItemForm
from apps.orders.models import Order, OrderItem
from django.views.generic.edit import CreateView


def orders_page(request):
    orders = Order.objects.all()
    print(orders)
    context = {"orders": orders}
    return render(request, "orders/index.html", context)


class PendingOrDone(TemplateView):
    template_name = "orders/pending_or_done_orders.html"


class PendingOrderListView(ListView):
    model = Order

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        orders = Order.objects.filter(status="P")
        return {"orders": orders}


class DoneOrderListView(ListView):
    model = Order

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        orders = Order.objects.filter(status="D")
        return {"orders": orders}


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    # template_name = 'customer_form.html'
    success_url = reverse_lazy("pending_order_list")


class OrderItemListView(DetailView):
    model = OrderItem

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        order_id = kwargs["object"].id
        order_items = OrderItem.objects.filter(order=order_id)
        return {"order_items": order_items}


class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    # template_name = 'customer_form.html'
    success_url = reverse_lazy("orderitem_list")
