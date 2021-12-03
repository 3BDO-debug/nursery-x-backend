from django.urls import path
from . import handlers


urlpatterns = [path("user-roles", handlers.user_roles_handler)]
