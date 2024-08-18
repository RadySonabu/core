# Generated by Django 4.2.14 on 2024-08-18 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EquipmentsInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("batch", models.CharField(default="", max_length=150, null=True)),
                ("branch", models.CharField(max_length=100, null=True)),
                ("name", models.CharField(max_length=150, null=True)),
                (
                    "description",
                    models.CharField(default="", max_length=500, null=True),
                ),
                ("is_working", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="RawMaterialsInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("batch", models.CharField(default="", max_length=150, null=True)),
                ("branch", models.CharField(max_length=100, null=True)),
                ("name", models.CharField(max_length=150, null=True)),
                (
                    "description",
                    models.CharField(default="", max_length=500, null=True),
                ),
                ("expiration", models.DateField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
