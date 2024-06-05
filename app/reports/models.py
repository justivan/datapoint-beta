from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from gwg.models import Reservation
from users.models import UserTrackingMixin

User = get_user_model()


class CaseType(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "reports_issue_case_type"
        ordering = ("name",)

    def __str__(self):
        return self.name


class IssueStatus(models.Model):
    name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = "reports_issue_status"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Issue(UserTrackingMixin, models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    case_type = models.ForeignKey(CaseType, on_delete=models.PROTECT)
    initial_cost = models.DecimalField(_("Error rate"), max_digits=11, decimal_places=4, default=0)
    final_cost = models.DecimalField(_("Final rate"), max_digits=11, decimal_places=4, default=0)
    hotel_cost = models.DecimalField(_("Contract rate"), max_digits=11, decimal_places=4, default=0)
    contributing_user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="%(class)s_contributed",
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="%(class)s_assigned",
    )
    status = models.ForeignKey(IssueStatus, on_delete=models.PROTECT)

    class Meta:
        db_table = "reports_issue"
        ordering = ("-created_at",)

    def __str__(self):
        return self.description
