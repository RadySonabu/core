# Generated by Django 4.2.14 on 2024-07-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="item",
            name="description",
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
