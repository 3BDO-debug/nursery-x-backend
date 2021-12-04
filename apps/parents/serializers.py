from rest_framework.serializers import ModelSerializer
from . import models


class ParentSerializer(ModelSerializer):
    class Meta:
        model = models.Parent
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ParentSerializer, self).to_representation(instance)
        representation["parent"] = {
            "fullname": f"{instance.parent_account.first_name} {instance.parent_account.last_name}",
            "profile_pic": instance.parent_account.profile_pic.url,
        }
        representation["email"] = instance.parent_account.email
        representation["phone_num"] = instance.parent_account.phone_num
        representation["address"] = instance.parent_account.address
        representation["account_type"] = instance.parent_account.account_type
        return representation
