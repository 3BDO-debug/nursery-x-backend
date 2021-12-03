from django.urls import path
from . import handlers


urlpatterns = [
    path('parents-data', handlers.parents_handler)
]
