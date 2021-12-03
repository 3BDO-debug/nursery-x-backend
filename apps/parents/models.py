from django.db import models
from accounts.models import User

# Create your models here.
class Parent(models.Model):
    parent_account = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Parent account", null=True
    )

    job = models.CharField(max_length=350, verbose_name="Job")
    qualification = models.CharField(max_length=350, verbose_name="Qualification")

    class Meta:
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return f"{self.parent_account.first_name} {self.parent_account.last_name}"
