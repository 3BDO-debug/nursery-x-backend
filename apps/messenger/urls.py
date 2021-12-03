from django.urls import path
from . import handlers

urlpatterns = [path("messages-data", handlers.messages_handler)]
