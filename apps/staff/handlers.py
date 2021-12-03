from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(["GET"])
def staff_members_handler(request):
    staff_members = models.StaffMember.objects.all()
    staff_members_serializer = serializers.StaffMemberSerializer(
        staff_members, many=True
    )
    return Response(data=staff_members_serializer.data, status=status.HTTP_200_OK)
