from rest_framework.serializers import ModelSerializer
from taggit.serializers import TagListSerializerField, TaggitSerializer
from . import models


class KidSerializer(TaggitSerializer, ModelSerializer):

    hobbies = TagListSerializerField()

    class Meta:
        model = models.Kid
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(KidSerializer, self).to_representation(instance)
        representation["profile_pic"] = instance.profile_pic.url
        representation["parent_id"] = instance.parent_account.parent_account.id
        representation[
            "parent_name"
        ] = f"{instance.parent_account.parent_account.first_name} {instance.parent_account.parent_account.last_name}"
        representation["parent_email"] = instance.parent_account.parent_account.email
        representation[
            "parent_phone_num"
        ] = instance.parent_account.parent_account.phone_num
        representation[
            "parent_address"
        ] = instance.parent_account.parent_account.address
        representation["parent_qualification"] = instance.parent_account.qualification
        representation["parent_job"] = instance.parent_account.job
        representation["attachment"] = instance.attachment.url

        return representation
