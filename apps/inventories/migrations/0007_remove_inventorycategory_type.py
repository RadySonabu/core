# Generated by Django 4.2.14 on 2024-08-22 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("inventories", "0006_inventorycategory_delete_inventory"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inventorycategory",
            name="type",
        ),
    ]
