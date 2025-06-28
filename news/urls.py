from django.urls import path

from news.api_endpoints import (
    NewsCreateAPIView,
    NewsListAPIView,
    NewsUpdateAPIView,
    NewsDeleteAPIView,
    MediaFileCreateAPIView,
    MediaFileListAPIView,
    MediaFileUpdateAPIView,
    MediaFileDeleteAPIView,
)

urlpatterns = [
    path("", NewsListAPIView.as_view(), name="news-list"),
    path("create/", NewsCreateAPIView.as_view(), name="news-create"),
    path("<slug:slug>/update/", NewsUpdateAPIView.as_view(), name="news-update"),
    path("<slug:slug>/delete/", NewsDeleteAPIView.as_view(), name="news-delete"),
    # Media files
    path("", MediaFileCreateAPIView.as_view(), name="media-create"),
    path("media/", MediaFileListAPIView.as_view(), name="media-list"),
    path("<int:pk>/update/", MediaFileUpdateAPIView.as_view(), name="media-update"),
    path("<int:pk>/delete/", MediaFileDeleteAPIView.as_view(), name="media-delete"),
]
