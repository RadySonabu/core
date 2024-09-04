from django.shortcuts import render

from apps.orders.models import Order


# Create your views here.
def home(request):
    orders = Order.objects.all()
    context = {"orders": orders}
    print(context)
    return render(request, "default/index.html", context)
