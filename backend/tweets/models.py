from django.db import models
from common.models import CommonModel


# Create your models here.
class Tweet(CommonModel):
    """Model Definition for Tweet"""

    payload = models.CharField(
        max_length=180,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="tweets",
    )

    def __str__(self):
        return f"{self.user} Tweet ...{self.payload[:10]}..."

    def like_count(self):
        return self.like.count()


class Like(CommonModel):
    """Model Definition for Like"""

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="likes",
    )
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete=models.CASCADE,
        related_name="likes",
    )

    def __str__(self):
        return f"{self.tweet.payload}"
