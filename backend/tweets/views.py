from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Tweet
from .serializers import TweetListSerializer, TweetDetailSerializer


# Create your views here.
class TweetListView(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetListSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            raise NotAuthenticated("Authentication required.")
        serializer = TweetDetailSerializer(data=request.data)
        if serializer.is_valid():
            tweet = serializer.save(user=request.user)
            return Response(TweetDetailSerializer(tweet).data)
        return Response(serializer.errors)
        


class TweetDetailView(APIView):
    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound("not found tweet")

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetDetailSerializer(tweet)
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise NotAuthenticated("not authenticated")
        serializer = TweetDetailSerializer(tweet, data=request.data, partial=True)
        if serializer.is_valid():
            updated_tweet = serializer.save()
            return Response(TweetDetailSerializer(updated_tweet).data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise NotAuthenticated("not authenticated")
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)