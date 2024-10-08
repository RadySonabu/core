from django import forms

from apps.branches.models import Branch
from apps.inventories.models import InventoryCategory, InventoryItem


class InventoryItemForm(forms.ModelForm):

    class Meta:
        model = InventoryItem
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description"].widget = forms.Textarea(
            attrs={
                "rows": 3,  # Adjust the number of rows
                "cols": 50,  # Adjust the number of columns
            }
        )

        default_branch = Branch.objects.get(name="BP1") # remove this hardcoded value
        self.fields["branch"].initial = default_branch
