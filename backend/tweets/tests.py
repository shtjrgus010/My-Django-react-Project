from rest_framework.test import APITestCase
from tweets.models import Tweet
from users.models import User
from rest_framework import status
from .serializers import TweetSerializer

class TestTweets(APITestCase):

    URL = "/api/v1/tweets/"

    def setUp(self):
        # Create a user
        user = User.objects.create_user(username="testuser", password="password")
        self.user = user

        # Create a sample tweet
        tweet = Tweet.objects.create(payload="Sample tweet", user=user)
        self.tweet = tweet

    def test_get_all_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["payload"], "Sample tweet")
        self.assertEqual(data[0]["user"], self.user.id)

    def test_create_tweet(self):
        self.client.login(username="testuser", password="password")

        response = self.client.post(self.URL, {"payload": "New tweet"})
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["payload"], "New tweet")
        self.assertEqual(data["user"], self.user.id)

    def test_create_tweet_unauthenticated(self):
        response = self.client.post(self.URL, {"payload": "Unauthorized tweet"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) 


class TestTweetDetail(APITestCase):

    def setUp(self):
        # Create a user
        user = User.objects.create_user(username="testuser", password="password")
        self.user = user

        # Create a sample tweet
        tweet = Tweet.objects.create(payload="Sample tweet", user=user)
        self.tweet = tweet

        # URL for the specific tweet
        self.detail_url = f"/api/v1/tweets/{self.tweet.pk}/"

    def test_get_tweet_detail(self):
        response = self.client.get(self.detail_url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["payload"], "Sample tweet")
        self.assertEqual(data["user"], self.user.id)

    def get(self, request, pk):
        tweet = self.get_object(pk)  
        serializer = TweetSerializer(tweet)
        return Response(serializer.data) 
    
    def test_update_tweet(self):
        self.client.login(username="testuser", password="password")

        response = self.client.put(self.detail_url, {"payload": "Updated tweet"})
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["payload"], "Updated tweet")

    def test_update_tweet_unauthenticated(self):
        response = self.client.put(self.detail_url, {"payload": "Unauthorized update"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_tweet(self):
        self.client.login(username="testuser", password="password")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # 200 → 204
        self.assertFalse(Tweet.objects.filter(pk=self.tweet.pk).exists())

    def test_update_tweet_unauthenticated(self):
        response = self.client.put(self.detail_url, {"payload": "Unauthorized update"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
