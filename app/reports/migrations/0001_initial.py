# Generated by Django 4.2.7 on 2024-03-04 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("gwg", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CaseType",
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
                ("name", models.CharField(max_length=120, unique=True)),
            ],
            options={
                "db_table": "reports_issue_case_type",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="IssueStatus",
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
                ("name", models.CharField(max_length=120, unique=True)),
            ],
            options={
                "db_table": "reports_issue_status",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "initial_cost",
                    models.DecimalField(decimal_places=4, default=0, max_digits=11),
                ),
                (
                    "final_cost",
                    models.DecimalField(decimal_places=4, default=0, max_digits=11),
                ),
                (
                    "hotel_cost",
                    models.DecimalField(decimal_places=4, default=0, max_digits=11),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_assigned",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "case_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="reports.casetype",
                    ),
                ),
                (
                    "contributing_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_contributed",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        db_column="created_by",
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="gwg.reservation",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="reports.issuestatus",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        db_column="updated_by",
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(class)s_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "reports_issue",
                "ordering": ("reservation__in_date",),
            },
        ),
    ]
