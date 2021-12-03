from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(["GET"])
def parents_handler(request):
    parents = models.Parent.objects.all()
    parents_serializer = serializers.ParentSerializer(parents, many=True)
    return Response(data=parents_serializer.data, status=status.HTTP_200_OK)
