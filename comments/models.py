from django.db import models
from django.conf import settings
from common.models import BaseModel
from news.models import News


class Comment(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="replies"
    )
    content = models.TextField()

    def __str__(self):
        return f"{self.user.email[:10]}: {self.content[:30]}"
