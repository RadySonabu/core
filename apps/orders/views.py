from django.shortcuts import render
from django.views.generic import ListView
from apps.orders.models import Order


# Create your views here.
def orders_page(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "orders/index.html", context)


# def add_orders_page(request):
class OrderListView(ListView):
    model = Order
