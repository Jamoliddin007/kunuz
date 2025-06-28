from django.db import models
from django.conf import settings
from common.models import BaseModel


class MediaFile(BaseModel):
    MEDIA_TYPES = (
        ("image", "Image"),
        ("video", "Video"),
        ("audio", "Audio"),
    )

    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    file = models.FileField(upload_to="media/")

    def __str__(self):
        return f"{self.media_type}: {self.file.name}"


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="news_list"
    )

    categories = models.ManyToManyField(Category, related_name="news_items", blank=True)
    tags = models.ManyToManyField(Tag, related_name="tagged_news", blank=True)

    default_image = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="default_news"
    )

    images = models.ManyToManyField(MediaFile, related_name="news_images", blank=True)

    is_active = models.BooleanField(default=True)
    is_scheduled = models.BooleanField(default=False)  # For Celery post scheduler
    publish_at = models.DateTimeField(null=True, blank=True)

    views_count = models.PositiveIntegerField(default=0)

    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_news",
        blank=True
    )

    def __str__(self):
        return self.title
