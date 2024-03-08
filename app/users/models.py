from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class BusinessUnit(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "users_business_unit"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class Deparment(models.Model):
    business_unit = models.ForeignKey(BusinessUnit, on_delete=models.PROTECT)
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "users_department"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"


class User(AbstractUser):
    name = models.CharField(_("Name of User"), max_length=120, blank=True)
    first_name = None
    last_name = None
    designation = models.CharField(max_length=120, blank=True, null=True)
    department = models.ForeignKey(Deparment, blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class UserTrackingMixin(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="%(class)s_created",
        db_column="created_by",
        editable=False,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="%(class)s_updated",
        db_column="updated_by",
        editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        current_user = kwargs.pop("current_user", None)
        print(current_user)
        if current_user:
            if not self.id:
                self.created_by = current_user
            self.updated_by = current_user
        super().save(*args, **kwargs)
