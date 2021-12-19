import cloudinary
from django.db import models
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager
from parents.models import Parent

# Create your models here.
class Kid(models.Model):
    parent_account = models.ForeignKey(
        Parent, on_delete=models.CASCADE, verbose_name="Parent account"
    )
    name = models.CharField(max_length=350, verbose_name="Name")
    profile_pic = CloudinaryField('image')
    birth_date = models.CharField(max_length=350, verbose_name="Birth date")
    gender = models.CharField(max_length=350, verbose_name="Gender")
    hobbies = TaggableManager(verbose_name="Hobbies")
    health_condition_notes = models.TextField(verbose_name="Health condition notes")
    attachment = models.FileField(
        upload_to="kids_attahcments", verbose_name="Attachment", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Kid"
        verbose_name_plural = "Kids"

    def __str__(self):
        return self.name
