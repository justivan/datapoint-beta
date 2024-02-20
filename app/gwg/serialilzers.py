from rest_framework import serializers
from .models import Reservation
from mapping.models import HotelMapping, OperatorMapping


class ReservationSerializer(serializers.ModelSerializer):
    hotel_name = serializers.SerializerMethodField()
    operator_name = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = (
            "status",
            "operator_name",
            "ref_id",
            "res_id",
            "bkg_ref",
            "operator_code",
            "hotel_name",
            "guest_name",
            "create_date",
            "sales_date",
            "in_date",
            "out_date",
            "room_type",
            "meal",
            "days",
            "adult",
            "child",
            "purchase_price",
            "sales_price",
        )

    def get_hotel_name(self, obj):
        try:
            mapping_hotel = HotelMapping.objects.get(external_code=obj.hotel_id)
            return mapping_hotel.hotel.name
        except HotelMapping.DoesNotExist:
            return None

    def get_operator_name(self, obj):
        try:
            mapping_operator = OperatorMapping.objects.get(external_code=obj.operator_id)
            return mapping_operator.operator.short_name
        except OperatorMapping.DoesNotExist:
            return None
