from django.db import models
from cloudinary.models import CloudinaryField
from staff.models import StaffMember
from kids.models import Kid
from accounts.models import User


class ActivityClass(models.Model):
    teacher = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, verbose_name="Teacher"
    )
    class_name = models.CharField(max_length=350, verbose_name="Class name")
    class_cover = CloudinaryField('image')
    class_members = models.ManyToManyField(Kid, verbose_name="Class member")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.class_name


class ClassActivity(models.Model):
    activity_class = models.ForeignKey(ActivityClass, on_delete=models.CASCADE)
    activity = models.CharField(max_length=350, verbose_name="Activity")
    activity_img = CloudinaryField('image')
    starts_at = models.TimeField(verbose_name="Starts at")

    class Meta:
        verbose_name = "Class activity"
        verbose_name_plural = "Class activities"

    def __str__(self):
        return self.activity


class ClassActivityRating(models.Model):
    activity_class = models.ForeignKey(
        ActivityClass, on_delete=models.CASCADE, verbose_name="Activity class"
    )
    activity = models.ForeignKey(ClassActivity, on_delete=models.CASCADE)
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE, verbose_name="Kid")
    rating = models.IntegerField(verbose_name="Rating")
    notes = models.TextField(verbose_name="Notes")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Class activity rating"
        verbose_name_plural = "Class activity ratings"


class ClassPost(models.Model):
    activity_class = models.ForeignKey(
        ActivityClass, on_delete=models.CASCADE, verbose_name="Activity class"
    )
    created_by = models.ForeignKey(
        StaffMember, on_delete=models.CASCADE, null=True, blank=True
    )
    post_body = models.TextField(verbose_name="Post body", null=True, blank=True)
    post_attachment = CloudinaryField('file')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Class post"
        verbose_name_plural = "Class posts"

    def __str__(self):
        return self.post_body


class ClassPostComment(models.Model):
    class_post = models.ForeignKey(
        ClassPost, on_delete=models.CASCADE, verbose_name="Class post"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Created by"
    )
    comment = models.TextField(verbose_name="Comment")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")

    class Meta:
        verbose_name = "Class post comment"
        verbose_name_plural = "Class post comments"

    def __str__(self):
        return self.comment
