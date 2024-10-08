# Generated by Django 4.2.14 on 2024-07-24 10:52

import apps.orders.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0004_order_mode_of_consumption_order_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_number",
            field=apps.orders.models.OrderNumberField(
                editable=False, max_length=8, unique=True
            ),
        ),
    ]
