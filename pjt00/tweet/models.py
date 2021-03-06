from django.db import models
from django.contrib.auth import get_user_model


class Tweet(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    tweet = models.TextField(max_length=140)
    def __str__(self):
        return self.tweet

class Favorite(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.tweet
