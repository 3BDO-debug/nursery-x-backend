from django.db import models

# Create your models here.
class UserRole(models.Model):
    role = models.CharField(max_length=350, verbose_name="Role")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "User role"
        verbose_name_plural = "User roles"

    def __str__(self):
        return self.role
