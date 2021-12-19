from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

# Create your models here.
class User(AbstractUser):
    account_type = models.CharField(max_length=350, verbose_name="Account type")
    gov_id = models.CharField(
        max_length=350,
        verbose_name="GOV ID",
    )
    phone_num = models.CharField(
        max_length=350,
        verbose_name="Phone number",
    )
    address = models.CharField(
        max_length=350,
        verbose_name="Address",
    )
    profile_pic = CloudinaryField('image')

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
