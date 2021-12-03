from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User
from . import models, serializers


@api_view(["GET", "POST"])
def messages_handler(request):

    if request.method == "POST":

        receiver = User.objects.get(id=int(request.data.get("receiverId")))

        models.Message.objects.create(
            initialized_between=request.user.id + receiver.id,
            sender=request.user,
            receiver=receiver,
            body=request.data.get("body"),
        ).save()

    messages = models.Message.objects.all()
    messages_serializer = serializers.MessageSerializer(messages, many=True)

    return Response(data=messages_serializer.data, status=status.HTTP_200_OK)
