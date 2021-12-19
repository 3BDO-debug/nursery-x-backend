from rest_framework.serializers import ModelSerializer
from . import models


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"

    def to_representation(self, instance):
        representation =  super(UserSerializer, self).to_representation(instance)   
        representation["profile_pic"] = instance.profile_pic.url
        representation["fullname"] = f"{instance.first_name} {instance.last_name}"
        return representation