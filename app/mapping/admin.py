from django.contrib import admin

from .models import HotelMapping, HotelRoomMapping, OperatorMapping


@admin.register(HotelMapping)
class HotelMappingAdmin(admin.ModelAdmin):
    list_display = (
        "external_code",
        "external_name",
        "hotel",
        "provider",
    )
    list_per_page = 20
    search_fields = ("hotel__id", "external_name")


@admin.register(HotelRoomMapping)
class HotelRoomMappingAdmin(admin.ModelAdmin):
    list_display = ("hotel_room", "provider", "external_code", "external_name")
    search_fields = ("hotel_room__hotel__id",)
    raw_id_fields = ("hotel_room",)
    autocomplete_lookup_fields = {"fk": ["hotel_room"]}


@admin.register(OperatorMapping)
class OperatorMappingAdmin(admin.ModelAdmin):
    list_display = ("operator", "external_code", "external_name")
