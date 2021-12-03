from django.urls import path
from . import handlers


urlpatterns = [path("meetings-data", handlers.meetings_handler)]
