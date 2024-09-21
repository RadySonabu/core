from typing import Any
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from apps.items.models import Item
from apps.orders.forms import OrderForm, OrderItemForm
from apps.orders.models import Order, OrderItem
from django.views.generic.edit import CreateView, UpdateView


def orders_page(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "orders/index.html", context)


class PendingOrDone(TemplateView):
    template_name = "orders/pending_or_done_orders.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return {
            'page': 'order',
        }

class PendingOrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        orders = Order.objects.filter(status="P")
        return {"orders": orders}


class DoneOrderListView(ListView):
    model = Order
    template_name = "orders/order_list.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        orders = Order.objects.filter(status="D")
        return {"orders": orders}


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    # template_name = 'customer_form.html'
    success_url = reverse_lazy("pending_order_list")


class OrderItemListView(DetailView):
    model = Order
    template_name = "orders/orderitem_detail.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        order_id = kwargs["object"].id
        order = Order.objects.get(pk=order_id)
        items = Item.objects.all()
        order_items = order.orderitem_set.all()
        total_price = order_items.aggregate(total=Sum('item__price'))
        return {
            "order_id": order_id,
            "items": items,
            "order_items": order_items,
            "total_price": total_price
        }


class OrderItemCreateView(CreateView):
    model = OrderItem
    form_class = OrderItemForm
    # success_url = reverse_lazy("orderitem_list", )

    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
        # Pass 'pk' from the URL to the form
        kwargs['initial']['pk'] = self.kwargs['pk']
        return kwargs
    
    def get_success_url(self):
        # Redirect to the order detail view, including the pk
        return reverse('orderitem_list', kwargs={'pk': self.kwargs['pk']})
    

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("pending_order_list")