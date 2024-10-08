# Generated by Django 4.2.14 on 2024-08-22 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("branches", "0005_alter_branch_options"),
        ("inventories", "0003_alter_equipmentsinventory_batch_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inventory",
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
                (
                    "batch",
                    models.CharField(
                        blank=True,
                        default="No batch provided",
                        max_length=150,
                        null=True,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Raw Materials", "Raw Materials"),
                            ("Equipments", "Equipments"),
                        ],
                        default="Raw Materials",
                        max_length=50,
                    ),
                ),
                ("name", models.CharField(max_length=150, null=True)),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        default="No description provided.",
                        max_length=500,
                        null=True,
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="branches.branch",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveField(
            model_name="rawmaterialsinventory",
            name="branch",
        ),
        migrations.DeleteModel(
            name="EquipmentsInventory",
        ),
        migrations.DeleteModel(
            name="RawMaterialsInventory",
        ),
    ]
