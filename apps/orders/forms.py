from django import forms

from apps.orders.models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["order"].widget = forms.Textarea(
        #     attrs={
        #         "rows": 3,  # Adjust the number of rows
        #         "cols": 50,  # Adjust the number of columns
        #     }
        # )
        self.pk = kwargs.pop('initial', None).pop('pk', None)
        order = Order.objects.get(pk=self.pk) # remove this hardcoded value
        self.fields["order"].initial = order
