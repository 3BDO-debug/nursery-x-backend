from rest_framework.serializers import ModelSerializer
from kids.serializers import KidSerializer
from . import models


class ActivityClassSerializer(ModelSerializer):
    class Meta:
        model = models.ActivityClass
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ActivityClassSerializer, self).to_representation(
            instance
        )
        representation[
            "teacher_name"
        ] = f"{instance.teacher.staff_account.first_name} {instance.teacher.staff_account.last_name}"
        representation[
            "teacher_profile_pic"
        ] = instance.teacher.staff_account.profile_pic.name
        representation["class_members_data"] = KidSerializer(
            instance.class_members.all(), many=True
        ).data
        return representation


class ClassActivitySerializer(ModelSerializer):
    class Meta:
        model = models.ClassActivity
        fields = "__all__"


class ClassActivityRatingSerializer(ModelSerializer):
    class Meta:
        model = models.ClassActivityRating
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ClassActivityRatingSerializer, self).to_representation(
            instance
        )
        representation["activity_class_name"] = instance.activity_class.class_name
        representation[
            "teacher_name"
        ] = f"{instance.activity_class.teacher.staff_account.first_name} {instance.activity_class.teacher.staff_account.last_name}"
        representation[
            "teacher_profile_pic"
        ] = instance.activity_class.teacher.staff_account.profile_pic.name
        representation["activity_name"] = instance.activity.activity
        return representation


class ClassPostSerializer(ModelSerializer):
    class Meta:
        model = models.ClassPost
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ClassPostSerializer, self).to_representation(instance)
        representation[
            "created_by_name"
        ] = f"{instance.created_by.staff_account.first_name} {instance.created_by.staff_account.last_name}"
        representation[
            "created_by_profile"
        ] = instance.created_by.staff_account.profile_pic.name
        return representation


class ClassPostCommentSerializer(ModelSerializer):
    class Meta:
        model = models.ClassPostComment
        fields = "__all__"

    def to_representation(self, instance):
        representation = super(ClassPostCommentSerializer, self).to_representation(
            instance
        )
        representation[
            "created_by_name"
        ] = f"{instance.created_by.first_name} {instance.created_by.last_name}"
        representation["created_by_profile_pic"] = instance.created_by.profile_pic.name
        return representation
