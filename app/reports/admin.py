from django.contrib import admin

from .models import CaseType, IssueStatus, Issue


@admin.register(CaseType)
class CaseTypeModelAdmin(admin.ModelAdmin):
    pass


@admin.register(IssueStatus)
class IssueStatusModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Issue)
class IssueModelAdmin(admin.ModelAdmin):
    list_display = (
        "reservation",
        "bkg_ref",
        "description",
        "case_type",
        "business_unit",
        "department",
        "contributing_user",
        "assigned_to",
        "initial_cost",
        "final_cost",
        "hotel_cost",
        "difference",
        "status",
    )
    readonly_fields = ("bkg_ref",)
    fieldsets = (
        ("Reservation Details", {"fields": ("reservation", "bkg_ref")}),
        ("Issue Details", {"fields": ("description", "case_type", "status")}),
        ("Cost Details", {"fields": ("initial_cost", "final_cost", "hotel_cost")}),
        ("User Details", {"fields": ("contributing_user", "assigned_to")}),
    )
    raw_id_fields = ("reservation",)
    autocomplete_lookup_fields = {
        "fk": ["reservation"],
    }

    def bkg_ref(self, obj):
        try:
            return obj.reservation.bkg_ref
        except AttributeError:
            return None

    def difference(self, obj):
        try:
            return obj.final_cost - obj.hotel_cost
        except AttributeError:
            return None

    def department(self, obj):
        try:
            return obj.contributing_user.department
        except AttributeError:
            return None

    def business_unit(self, obj):
        try:
            return obj.contributing_user.department.business_unit
        except AttributeError:
            return None

    def save_model(self, request, obj, form, change):
        if not obj.id:  # New hotel creation
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related(
                "reservation",
                "case_type",
                "contributing_user",
                "assigned_to",
                "status",
            )
        )
