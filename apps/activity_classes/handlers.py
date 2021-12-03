from dateutil.parser import parse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from staff.models import StaffMember
from kids.models import Kid
from . import models, serializers


@api_view(["GET", "POST", "PUT"])
def activity_classes_handler(request):
    if request.method == "POST":

        teacher = StaffMember.objects.get(staff_account=request.user)

        models.ActivityClass.objects.create(
            teacher=teacher,
            class_name=request.data.get("className"),
            class_cover=request.data.get("classCover"),
        ).save()

    elif request.method == "PUT":
        activity_class = models.ActivityClass.objects.get(
            id=int(request.data.get("classId"))
        )
        member = models.Kid.objects.get(id=int(request.data.get("kidId")))

        if member in activity_class.class_members.all():

            activity_class.class_members.remove(member.id)
        else:
            activity_class.class_members.add(member)

        activity_class.save()

    activity_classes = models.ActivityClass.objects.all().order_by("-created_at")
    activity_classes_serializer = serializers.ActivityClassSerializer(
        activity_classes, many=True
    )
    return Response(data=activity_classes_serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def class_activities_handler(request, class_id):
    activity_class = models.ActivityClass.objects.get(id=class_id)

    if request.method == "POST":

        models.ClassActivity.objects.create(
            activity_class=activity_class,
            activity=request.data.get("activity"),
            activity_img=request.data.get("activityImg"),
            starts_at=parse(request.data.get("startsAt")).time(),
        ).save()

    class_activities = models.ClassActivity.objects.filter(
        activity_class=activity_class
    )
    class_activities_serializer = serializers.ClassActivitySerializer(
        class_activities, many=True
    )
    return Response(data=class_activities_serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def class_activity_ratings_handler(request):

    if request.method == "POST":

        models.ClassActivityRating.objects.create(
            activity_class=models.ActivityClass.objects.get(
                id=int(request.data.get("classId"))
            ),
            activity=models.ClassActivity.objects.get(
                id=int(request.data.get("activityId"))
            ),
            kid=Kid.objects.get(id=int(request.data.get("kidId"))),
            rating=int(request.data.get("rating")),
            notes=request.data.get("notes"),
        ).save()

        return Response(
            status=status.HTTP_201_CREATED,
        )

    elif request.method == "GET":

        kid = Kid.objects.get(id=int(request.GET.get("kidId")))

        activity_ratings = models.ClassActivityRating.objects.filter(kid=kid).order_by(
            "-created_at"
        )
        activity_ratings_serializer = serializers.ClassActivityRatingSerializer(
            activity_ratings, many=True
        )

        return Response(
            status=status.HTTP_200_OK, data=activity_ratings_serializer.data
        )


@api_view(["GET", "POST"])
def class_posts_handlers(request, class_id):
    activity_class = models.ActivityClass.objects.get(id=class_id)

    if request.method == "POST":
        models.ClassPost.objects.create(
            created_by=StaffMember.objects.get(staff_account=request.user),
            activity_class=activity_class,
            post_body=request.data.get("postBody"),
            post_attachment=request.data.get("postAttachment"),
        ).save()

    class_posts = models.ClassPost.objects.filter(
        activity_class=activity_class
    ).order_by("-created_at")
    class_posts_serializer = serializers.ClassPostSerializer(class_posts, many=True)
    return Response(data=class_posts_serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST"])
def class_post_comments_handler(request, class_post_id):
    class_post = models.ClassPost.objects.get(id=class_post_id)

    if request.method == "POST":
        models.ClassPostComment.objects.create(
            class_post=class_post,
            created_by=request.user,
            comment=request.data.get("comment"),
        ).save()

    class_post_comments = models.ClassPostComment.objects.filter(
        class_post=class_post
    ).order_by("-created_at")
    class_post_comments_serializer = serializers.ClassPostCommentSerializer(
        class_post_comments, many=True
    )
    return Response(data=class_post_comments_serializer.data, status=status.HTTP_200_OK)
