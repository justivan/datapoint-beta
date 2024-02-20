from rest_framework import serializers
from definitions.serializers import AreaSerializer
from .models import (
    PurchaseManager,
    SalesContact,
    HotelChain,
    HotelCategory,
    HotelStatus,
    HotelTag,
    Hotel,
    HotelRoom,
)


class PurchaseManagerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.name", read_only=True)  # Custom field to get user's name

    class Meta:
        model = PurchaseManager
        fields = ("id", "user")


class SalesContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesContact
        fields = ("id", "name", "designation", "email", "mobile")


class HotelChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelChain
        fields = ("id", "name")


class HotelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelCategory
        fields = ("id", "name")


class HotelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelStatus
        fields = ("id", "name")


class HotelTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelTag
        fields = ("id", "name", "slug")


class HotelSerializer(serializers.ModelSerializer):
    category = HotelCategorySerializer()
    area = AreaSerializer()
    chain = HotelChainSerializer()
    sales_contact = SalesContactSerializer()
    purchase_manager = PurchaseManagerSerializer()
    status = HotelStatusSerializer()
    tags = HotelTagSerializer(many=True)

    class Meta:
        model = Hotel
        fields = (
            "id",
            "name",
            "category",
            "chain",
            "area",
            "latitude",
            "longitude",
            "sales_contact",
            "purchase_manager",
            "status",
            "giata",
            "tags",
        )
