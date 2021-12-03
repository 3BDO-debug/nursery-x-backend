from django.db import models
from accounts.models import User

# Create your models here.
class StaffMember(models.Model):
    staff_account = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Staff account"
    )
    role = models.CharField(max_length=350, verbose_name="Role")

    class Meta:
        verbose_name = "Staff member"
        verbose_name_plural = "Staff"

    def __str__(self):
        return f"{self.staff_account.first_name} {self.staff_account.last_name} - {self.role}"
