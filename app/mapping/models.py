from django.db import models
from django.utils.translation import gettext_lazy as _

from accommodation.models import Hotel, HotelRoom
from clients.models import Operator


class Provider(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class HotelMapping(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        verbose_name=_("Master Hotel Name"),
        on_delete=models.PROTECT,
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.PROTECT,
        default=1,
    )
    external_code = models.BigIntegerField()
    external_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("hotel__name", "external_name")
        db_table = "mapping_hotel"
        unique_together = ("provider", "external_code")
        verbose_name_plural = "hotels"

    def __str__(self):
        return f"{self.external_name}"


class HotelRoomMapping(models.Model):
    hotel_room = models.ForeignKey(
        HotelRoom,
        verbose_name=_("Master Room Name"),
        on_delete=models.PROTECT,
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.PROTECT,
        default=1,
    )
    external_code = models.CharField(max_length=255)
    external_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("hotel_room__hotel__name", "hotel_room")
        db_table = "mapping_hotel_room"
        unique_together = (("hotel_room", "provider", "external_code"),)
        verbose_name_plural = "rooms"

    def __str__(self):
        return f"{self.external_code}: {self.external_name}"


class OperatorMapping(models.Model):
    operator = models.ForeignKey(
        Operator,
        verbose_name=_("Master Operator Name"),
        on_delete=models.PROTECT,
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.PROTECT,
        default=1,
    )
    external_code = models.IntegerField()
    external_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("external_name",)
        db_table = "mapping_operator"
        unique_together = (("provider", "external_code"),)
        verbose_name_plural = "operators"

    def __str__(self):
        return f"{self.external_code}: {self.external_name}"
