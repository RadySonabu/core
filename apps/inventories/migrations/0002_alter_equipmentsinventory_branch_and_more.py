# Generated by Django 4.2.14 on 2024-08-18 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("branches", "0004_alter_branch_description"),
        ("inventories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equipmentsinventory",
            name="branch",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="branches.branch",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="rawmaterialsinventory",
            name="branch",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="branches.branch",
            ),
            preserve_default=False,
        ),
    ]
