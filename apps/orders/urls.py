from django.urls import path
from . import views

urlpatterns = [
    # path("", views.orders_page),
    path("", views.OrderListView.as_view()),
]
