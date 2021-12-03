from django.urls import path
from . import handlers


urlpatterns = [
    path("activity-classes-data", handlers.activity_classes_handler),
    path("class-activities/<int:class_id>", handlers.class_activities_handler),
    path("class-activity-ratings", handlers.class_activity_ratings_handler),
    path("class-posts/<int:class_id>", handlers.class_posts_handlers),
    path(
        "class-post-comments/<int:class_post_id>", handlers.class_post_comments_handler
    ),
]
