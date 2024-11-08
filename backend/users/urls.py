from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_pk>/tweets", views.TweetsByUser.as_view()),
]
