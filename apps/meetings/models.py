from django.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=350, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    start_date = models.DateTimeField(verbose_name="Start date")
    end_date = models.DateTimeField(verbose_name="End date", null=True, blank=True)

    class Meta:
        verbose_name = "Meeting"
        verbose_name_plural = "Meetings"

    def __str__(self):
        return self.title
