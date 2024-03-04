from django.contrib import admin
from .models import (
    Hotel,
    HotelStatus,
    HotelChain,
    HotelRoom,
    PurchaseManager,
    SalesContact,
    HotelTag,
)

from mapping.models import HotelMapping, HotelRoomMapping


class HotelMappingInline(admin.TabularInline):
    model = HotelMapping
    extra = 0


class HotelRoomInline(admin.TabularInline):
    model = HotelRoom
    extra = 0


class HotelRoomMappingInline(admin.TabularInline):
    model = HotelRoomMapping
    extra = 0


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "chain",
        "country",
        "region",
        "area",
        "latitude",
        "longitude",
        "purchase_manager",
        "sales_contact",
        "giata",
        "get_tags",
        "updated_at",
        "updated_by",
        "status",
    )
    list_filter = ("area__region__country", "area__region", "area", "chain", "status", "purchase_manager")
    list_per_page = 20
    search_fields = ("id", "name", "giata", "chain__name")
    inlines = (
        HotelMappingInline,
        HotelRoomInline,
    )
    fieldsets = (
        ("General Information", {"fields": ("name", "category", "chain")}),
        ("Location", {"fields": ("area", "latitude", "longitude")}),
        ("Contacts", {"fields": ("sales_contact", "purchase_manager")}),
        ("Additional Information", {"fields": ("status", "tags", "giata")}),
    )

    raw_id_fields = ("area", "tags", "sales_contact")
    autocomplete_lookup_fields = {
        "fk": ["area", "sales_contact"],
        "m2m": ["tags"],
    }

    def country(self, obj):
        try:
            return obj.area.region.country
        except AttributeError:
            return None

    def region(self, obj):
        try:
            return obj.area.region.name
        except AttributeError:
            return None

    def get_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    def save_model(self, request, obj, form, change):
        if not obj.id:  # New hotel creation
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    get_tags.short_description = "Tags"

    def get_queryset(self, request):
        return (
            super()
            .get_queryset(request)
            .select_related(
                "category",
                "area",
                "area__region",
                "area__region__country",
                "chain",
                "sales_contact",
                "purchase_manager",
                "purchase_manager__user",
                "status",
            )
            .prefetch_related("tags")
        )


@admin.register(PurchaseManager)
class PurchaseManagerAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    ordering = ("user__name",)

    def name(self, obj):
        return f"{obj.user.name}"

    def email(self, obj):
        return obj.user.email


@admin.register(SalesContact)
class SalesContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "designation", "email", "mobile")


@admin.register(HotelStatus)
class HotelStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelChain)
class HotelChainAdmin(admin.ModelAdmin):
    pass


@admin.register(HotelTag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    inlines = (HotelRoomMappingInline,)  # , RoomInventoryInline)
    list_display = ("id", "name", "hotel", "ordinal", "room_mapping")
    search_fields = ("hotel__name", "hotel__id")
    list_editable = ("ordinal",)
    raw_id_fields = ("hotel",)
    autocomplete_lookup_fields = {"fk": ["hotel"]}

    def room_mapping(self, obj):
        mapping = HotelRoomMapping.objects.filter(hotel_room=obj)
        rooms = ", ".join(f"({room.external_code}) {room.external_name}" for room in mapping)
        return rooms if rooms else "-"
