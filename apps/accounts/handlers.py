import asyncio, json, time
from asgiref.sync import sync_to_async
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework_simplejwt.tokens import RefreshToken
from parents.models import Parent
from staff.models import StaffMember
from . import models, serializers


@api_view(["POST"])
@permission_classes([])
@permission_classes([])
def register_handler(request):
    request_data = json.loads(request.data.get("values"))
    request_files = request.data.get("files")
    user = models.User.objects.create_user(
        first_name=request_data["firstName"],
        last_name=request_data["lastName"],
        username=request_data["username"],
        email=request_data["email"],
        password=request_data["password"],
        account_type=request_data["accountType"],
        gov_id=request_data["govId"],
        phone_num=request_data["phoneNumber"],
        address=request_data["address"],
        profile_pic=request_files,
    )

    if user.account_type == "staff-member":
        StaffMember.objects.create(staff_account=user, role=request_data["role"]).save()
    elif user.account_type == "parent":
        Parent.objects.create(
            parent_account=user,
            job=request_data["job"],
            qualification=request_data["qualification"],
        ).save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(["GET"])
def user_info_handler(request):
    user_info = models.User.objects.get(id=request.user.id)
    user_info_serializer = serializers.UserSerializer(user_info, many=False)
    return Response(status=status.HTTP_200_OK, data=user_info_serializer.data)


@api_view(["POST"])
def logout_handler(request):
    refresh_token = request.data.get("refresh_token")
    token = RefreshToken(refresh_token)
    token.blacklist()
    return Response(status=status.HTTP_205_RESET_CONTENT)
