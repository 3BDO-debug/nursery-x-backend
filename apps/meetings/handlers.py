from dateutil.parser import parse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


@api_view(["GET", "POST"])
def meetings_handler(request):

    if request.method == "POST":
        models.Meeting.objects.create(
            title=request.data.get("title"),
            description=request.data.get("description"),
            start_date=parse(request.data.get("startDate")),
            end_date=parse(request.data.get("endDate")),
        ).save()

    meetings = models.Meeting.objects.all()
    meetings_serializer = serializers.MeetingSerializer(meetings, many=True)
    return Response(data=meetings_serializer.data, status=status.HTTP_200_OK)
