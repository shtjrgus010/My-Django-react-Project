from rest_framework import serializers
from .models import Tweet
from users.serializers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)  # 사용자 ID만 반환

    class Meta:
        model = Tweet
        fields = "__all__"

