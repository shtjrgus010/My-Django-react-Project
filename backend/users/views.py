from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer
from tweets.models import Tweet
from tweets.serializers import TweetListSerializer

# 유저 리스트 조회
class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

# 특정 유저 상세 조회
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound("사용자를 찾을 수 없습니다.")

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

# 특정 유저의 트윗 조회
class TweetsByUser(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetListSerializer(tweets, many=True)
        return Response(serializer.data)
