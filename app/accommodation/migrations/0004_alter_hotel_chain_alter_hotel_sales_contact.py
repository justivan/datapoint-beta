# Generated by Django 4.2.7 on 2024-03-03 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accommodation", "0003_alter_hotel_options_alter_hotel_latitude_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hotel",
            name="chain",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="accommodation.hotelchain",
            ),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="sales_contact",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="accommodation.salescontact",
            ),
        ),
    ]
