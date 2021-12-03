from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework import status
from rest_framework.response import Response
from . import models, serializers


@api_view(["GET"])
@permission_classes([])
@permission_classes([])
def user_roles_handler(request):
    user_roles = models.UserRole.objects.all()
    user_roles_serializer = serializers.UserRoleSerializer(user_roles, many=True)
    return Response(status=status.HTTP_200_OK, data=user_roles_serializer.data)
