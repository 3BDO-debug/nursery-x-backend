from django.urls import path
from . import handlers

urlpatterns = [path("kids-data", handlers.kids_handler)]
