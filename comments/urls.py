from django.urls import path
from comments.api_endpoints import (
    CommentCreateAPIView,
    CommentListAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView,
)

urlpatterns = [
    path("", CommentListAPIView.as_view(), name="comment-list"),
    path("create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path("<int:pk>/update/", CommentUpdateAPIView.as_view(), name="comment-update"),
    path("<int:pk>/delete/", CommentDeleteAPIView.as_view(), name="comment-delete"),
]
