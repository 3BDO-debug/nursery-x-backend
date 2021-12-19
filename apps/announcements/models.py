from django.db import models
from cloudinary.models import CloudinaryField
from staff.models import StaffMember


class Announcement(models.Model):
    created_by = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, verbose_name="Created by"
    )
    title = models.CharField(max_length=350, verbose_name="Title")
    cover = CloudinaryField('image')
    body = models.TextField(verbose_name="Body")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    is_featured = models.BooleanField(default=False, verbose_name="Is featured")

    class Meta:
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"

    def __str__(self):
        return self.title
