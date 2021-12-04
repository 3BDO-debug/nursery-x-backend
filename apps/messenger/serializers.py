from rest_framework.serializers import ModelSerializer
from . import models


class MessageSerializer(ModelSerializer):
    class Meta:
        model = models.Message
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(MessageSerializer, self).to_representation(instance)
        representation["sender_profile_pic"] = instance.sender.profile_pic.url
        return representation
