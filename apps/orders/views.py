from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from apps.orders.forms import OrderForm
from apps.orders.models import Order
from django.views.generic.edit import CreateView

# from django.views.generic.edit import CreateView


# Create your views here.
def orders_page(request):
    orders = Order.objects.all()
    print(orders)
    context = {"orders": orders}
    return render(request, "orders/index.html", context)


# def add_orders_page(request):
class OrderListView(ListView):
    model = Order

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        orders = Order.objects.all()
        return {"orders": orders}


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    # template_name = 'customer_form.html'
    success_url = reverse_lazy("order_list")
