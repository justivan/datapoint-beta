# Generated by Django 4.2.7 on 2023-12-20 09:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accommodation", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER SEQUENCE accommodation_hotel_id_seq RESTART WITH 10000001;",
        )
    ]