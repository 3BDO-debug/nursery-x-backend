from django.urls import path
from . import handlers


urlpatterns = [
    path('staff-members', handlers.staff_members_handler)
]
