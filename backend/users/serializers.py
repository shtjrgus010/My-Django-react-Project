from rest_framework.serializers import ModelSerializer
from .models import User
from tweets.serializers import TweetListSerializer


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username"]


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "username",
        )


class UserDetailSerializer(ModelSerializer):
    tweets = TweetListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "pk",
            "username",
            "first_name",
            "last_name",
            "tweets",
        )
