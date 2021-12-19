from rest_framework.serializers import ModelSerializer
from . import models


class AnnouncementSerializer(ModelSerializer):
    class Meta:
        model = models.Announcement
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(AnnouncementSerializer, self).to_representation(instance)
        representation[
            "created_by_name"
        ] = f"{instance.created_by.staff_account.first_name} {instance.created_by.staff_account.last_name}"
        representation[
            "created_by_profile_pic"
        ] = instance.created_by.staff_account.profile_pic.url
        representation["cover"] = instance.cover.url
        return representation
