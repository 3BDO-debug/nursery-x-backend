from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from staff.models import StaffMember
from . import models, serializers


@api_view(["GET", "POST"])
def announcements_handler(request):

    if request.method == "POST":
        staff_member = StaffMember.objects.get(staff_account=request.user.id)

        models.Announcement.objects.create(
            created_by=staff_member,
            title=request.data.get("title"),
            cover=request.data.get("cover"),
            body=request.data.get("body"),
            is_featured=bool(request.data.get("isFeatured")),
        ).save()

    announcements = models.Announcement.objects.all().order_by("-created_at")
    announcements_serializer = serializers.AnnouncementSerializer(
        announcements, many=True
    )
    return Response(data=announcements_serializer.data, status=status.HTTP_200_OK)
