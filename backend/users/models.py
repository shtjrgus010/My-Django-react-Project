from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """ User Model """
    
    first_name = models.CharField(editable=False, max_length=150)
    last_name = models.CharField(editable=False, max_length=150)
    name = models.CharField(max_length=150)
