from rest_framework.serializers import ModelSerializer
from . import models


class MeetingSerializer(ModelSerializer):
    class Meta:
        model = models.Meeting
        fields = "__all__"
