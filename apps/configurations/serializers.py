from rest_framework.serializers import ModelSerializer
from . import models


class UserRoleSerializer(ModelSerializer):
    class Meta:
        model = models.UserRole
        fields = "__all__"
