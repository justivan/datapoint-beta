from django.db import models

# from accommodation.models import Hotel, HotelRoom
# from definitions.models import MealPlan
# from clients.models import Operator


class Reservation(models.Model):
    ref_id = models.IntegerField(primary_key=True)
    res_id = models.IntegerField()
    hotel_id = models.IntegerField()
    operator_id = models.IntegerField()
    operator_code = models.CharField(max_length=20)
    bkg_ref = models.CharField(max_length=100)
    guest_name = models.CharField(max_length=100, blank=True, null=True)
    sales_date = models.DateField()
    in_date = models.DateField()
    out_date = models.DateField()
    room_type = models.CharField(max_length=120, blank=True, null=True)
    room_code = models.CharField(max_length=3, blank=True, null=True)
    meal = models.CharField(max_length=3, blank=True, null=True)
    adult = models.IntegerField()
    child = models.IntegerField()
    days = models.IntegerField()
    purchase_price = models.DecimalField(max_digits=11, decimal_places=4, default=0)
    purchase_currency = models.CharField(max_length=3, blank=True, null=True)
    sales_price = models.DecimalField(max_digits=11, decimal_places=4, default=0)
    sales_currency = models.CharField(max_length=3, blank=True, null=True)
    purchase_price_indicator = models.CharField(max_length=20, blank=True, null=True)
    sales_price_indicator = models.CharField(max_length=20, blank=True, null=True)
    create_date = models.DateField()
    last_modified_date = models.DateField()
    cancellation_date = models.DateField(blank=True, null=True)
    purchase_contract_id = models.IntegerField(blank=True, null=True, default=0)
    purchase_spo_id = models.IntegerField(blank=True, null=True, default=0)
    purchase_spo_name = models.TextField(blank=True, null=True)
    purchase_spo_code = models.TextField(blank=True, null=True)
    sales_contract_id = models.IntegerField(blank=True, null=True, default=0)
    sales_spo_id = models.IntegerField(blank=True, null=True, default=0)
    sales_spo_name = models.TextField(blank=True, null=True)
    sales_spo_code = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=3)
    status4 = models.CharField(max_length=3)
    status5 = models.CharField(max_length=3)

    class Meta:
        ordering = ("in_date",)
