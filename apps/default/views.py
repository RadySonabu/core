from django.shortcuts import render

from apps.orders.models import Order


# Create your views here.
def home(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    return render(request, "default/index.html", context)
