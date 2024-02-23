from django.db import models
from django.db.models.functions import Lower
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from definitions.models import Area
from users.models import UserTrackingMixin

User = get_user_model()


class PurchaseManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table = "accommodation_purchase_manager"
        ordering = ("user__name",)

    def __str__(self):
        return f"{self.user.name}"


class SalesContact(models.Model):
    name = models.CharField(_("Name of Contact"), max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=120, unique=True)
    mobile = PhoneNumberField(blank=True, null=True)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains", "email__icontains")

    class Meta:
        db_table = "accommodation_sales_contact"
        ordering = ("name",)

    def __str__(self):
        return f"{self.email}"


class HotelChain(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "accommodation_hotel_chain"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class HotelCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "accommodation_hotel_category"
        ordering = ("name",)
        verbose_name_plural = "hotel categories"

    def __str__(self):
        return f"{self.name}"


class HotelStatus(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "accommodation_hotel_status"
        ordering = ("name",)
        verbose_name_plural = "hotel status"

    def __str__(self):
        return f"{self.name}"


class HotelTag(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, editable=False)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains")

    class Meta:
        db_table = "accommodation_tag"
        ordering = ("name",)

    def __str__(self):
        return f"{self.slug}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Hotel(UserTrackingMixin, models.Model):
    name = models.CharField(_("Hotel Name"), max_length=120, unique=True)
    category = models.ForeignKey(HotelCategory, on_delete=models.PROTECT)
    area = models.ForeignKey(
        Area,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    latitude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        blank=True,
        null=True,
    )
    longitude = models.DecimalField(
        max_digits=11,
        decimal_places=8,
        blank=True,
        null=True,
    )
    chain = models.ForeignKey(
        HotelChain,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    sales_contact = models.ForeignKey(
        SalesContact,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    purchase_manager = models.ForeignKey(
        PurchaseManager,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    status = models.ForeignKey(HotelStatus, default=1, on_delete=models.PROTECT)
    giata = models.IntegerField(blank=True, default=0)
    tags = models.ManyToManyField(
        HotelTag,
        db_table="accommodation_hotel_tag",
        blank=True,
    )

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains")

    class Meta:
        ordering = ("area__region__country__name", Lower("name"))

    def __str__(self):
        return self.name


class HotelRoom(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        verbose_name=_("Master Hotel Name"),
        on_delete=models.PROTECT,
        db_index=True,
    )
    name = models.CharField(_("Hotel Room Name"), max_length=120)
    ordinal = models.PositiveIntegerField(default=1)

    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "name__icontains", "hotel__name__icontains")

    class Meta:
        ordering = ("hotel", "ordinal")
        db_table = "accommodation_hotel_room"
        unique_together = (("hotel", "name"),)

    def __str__(self):
        return f"{self.name}"
