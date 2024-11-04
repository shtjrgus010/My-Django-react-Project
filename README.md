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
