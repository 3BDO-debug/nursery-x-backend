from rest_framework.serializers import ModelSerializer
from . import models


class StaffMemberSerializer(ModelSerializer):
    class Meta:
        model = models.StaffMember
        fields = "__all__"

    def to_representation(self, instance):
        representaion = super(StaffMemberSerializer, self).to_representation(instance)
        representaion[
            "fullname"
        ] = f"{instance.staff_account.first_name} {instance.staff_account.last_name}"
        representaion["profile_pic"] = instance.staff_account.profile_pic.url
        representaion["email"] = instance.staff_account.email
        representaion["phone_num"] = instance.staff_account.phone_num
        representaion["address"] = instance.staff_account.address
        representaion["date_joined"] = instance.staff_account.date_joined
        representaion["account_type"] = instance.staff_account.account_type
        return representaion
