from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.shortcuts import get_object_or_404
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


class TweetsByUser(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
