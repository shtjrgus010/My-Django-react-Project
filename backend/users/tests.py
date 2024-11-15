from rest_framework.test import APITestCase
from . import models


# Create your tests here.
class TestTweets(APITestCase):
    NAME = "Tweet Test"
    DESC = "Tweet Desc"
    URL = "/api/v1/tweets/"

    def setUp(self):
        models.Tweet.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_tweets(self):
        response = self.client.get("/api/v1/tweets/")

        data = response.json()
