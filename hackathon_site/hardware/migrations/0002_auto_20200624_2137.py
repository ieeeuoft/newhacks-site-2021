# Generated by Django 3.0.5 on 2020-06-25 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("hardware", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="incident",
            name="order",
        ),
        migrations.RemoveField(
            model_name="order",
            name="hardware",
        ),
        migrations.RemoveField(
            model_name="order",
            name="part_returned_health",
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("Cart", "Cart"),
                    ("Submitted", "Submitted"),
                    ("Ready for Pickup", "Ready for Pickup"),
                    ("Picked Up", "Picked Up"),
                ],
                default="Cart",
                max_length=64,
            ),
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "part_returned_health",
                    models.CharField(
                        choices=[
                            ("Healthy", "Healthy"),
                            ("Heavily Used", "Heavily Used"),
                            ("Broken", "Broken"),
                            ("Lost", "Lost"),
                        ],
                        max_length=64,
                        null=True,
                    ),
                ),
                (
                    "hardware",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_items",
                        to="hardware.Hardware",
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="hardware.Order",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="incident",
            name="order_item",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="incident",
                to="hardware.OrderItem",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="hardware_set",
            field=models.ManyToManyField(
                through="hardware.OrderItem", to="hardware.Hardware"
            ),
        ),
    ]
