from rest_framework import serializers
from .models import Tweet


class TweetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["pk", "payload", "created_at"]


class TweetDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tweet
        fields = "__all__"
        depth = 1
