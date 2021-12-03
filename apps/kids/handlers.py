import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from parents.models import Parent
from . import models, serializers


@api_view(["GET", "POST"])
def kids_handler(request):

    if request.method == "POST":
        request_data = json.loads(request.data.get("values"))

        parent_account = Parent.objects.get(
            parent_account=int(request_data["parentId"])
        )

        kid = models.Kid.objects.create(
            parent_account=parent_account,
            name=request_data["name"],
            profile_pic=request.data.get("profilePic"),
            birth_date=request_data["birthDate"],
            gender=request_data["gender"],
            health_condition_notes=request_data["healthConditionNotes"],
            attachment=request.data.get("attachment"),
        )

        kid.hobbies.set(request_data["hobbies"])
        kid.save()

    kids = models.Kid.objects.all().order_by("-created_at")
    kids_serializer = serializers.KidSerializer(kids, many=True)
    return Response(data=kids_serializer.data, status=status.HTTP_200_OK)
