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
        # "allocation_group",
    )
    list_filter = ("name", "category")
    search_fields = ("name",)
    inlines = (OperatorMappingInline,)


@admin.register(OperatorGroup)
class OperatorGroupModelAdmin(admin.ModelAdmin):
    list_display = ("name",)
