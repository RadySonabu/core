# Generated by Django 4.2.14 on 2024-07-24 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0002_item_quantity_alter_item_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="quantity",
        ),
    ]
