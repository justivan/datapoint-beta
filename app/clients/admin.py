from django.contrib import admin

from .models import Operator, OperatorGroup
from mapping.models import OperatorMapping


class OperatorMappingInline(admin.TabularInline):
    model = OperatorMapping
    extra = 0


@admin.register(Operator)
class OperatorModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "short_name",
        "category",
        "operator_group",
        "operator_mapping",
        # "allocation_group",
    )
    list_filter = ("name", "category")
    search_fields = ("name",)
    inlines = (OperatorMappingInline,)

    def operator_mapping(self, obj):
        mapping = OperatorMapping.objects.filter(operator=obj)
        operators = ", ".join(f"({operator.external_code}) {operator.external_name}" for operator in mapping)
        return operators if operators else "-"


@admin.register(OperatorGroup)
class OperatorGroupModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
