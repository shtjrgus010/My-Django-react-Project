# My Project

## 2024.11.01

### Common Model Field

- created_at
- updated_at

### Tweet Model Field

- payload(max_length=180)
- user: ForeignKey

### Like Model Field

- user: ForeignKey
- tweet: ForeignKey

### Requirements

- Use `abstract` classes
- Customize the `__str__` method of all classes.

## 2024.11.04

- related_name 사용

```python
tweet = Tweet.objects.get(id=1)
tweet.like_set.count()
```

```python
# related_name
class Like(CommonModel):
    tweet = models.ForeignKey(
        "tweets.Tweet",
        on_delete = models.CASCADE,
        related_name="like",
    )

tweet = Tweet.objects.get(id=1)
tweet.like.count()
```

## 2024.11.05

- Like Admin

* Search by username of user foreign key.
* Filter by created_at

- Tweet Admin: (개선필요사항)

* Search by payload
* Search by username of user foreign key.
* Filter by created_at
* Make a CUSTOM filter for Tweets that contain and don't contain the words Elon Musk

## 2024.11.08

### Misson

- Refactor all the serializers to use ModelSerializer.
- Refactor all the views to use APIView.

## 2024.11.12

### Django REST Framework 사용하여 API 구축

Tweets 관련 API

`GET /api/v1/tweets`: 모든 트윗 조회
`POST /api/v1/tweets`: 새 트윗 생성
`GET /api/v1/tweets/<int:pk>`: 특정 트윗 조회
`PUT /api/v1/tweets/<int:pk>`: 특정 트윗 수정
`DELETE /api/v1/tweets/<int:pk>`: 특정 트윗 삭제
Users 관련 API

`GET /api/v1/users`: 모든 유저 조회
`GET /api/v1/users/<int:pk>`: 특정 유저 조회
`GET /api/v1/users/<int:pk>/tweets`: 특정 유저가 작성한 트윗 조회
