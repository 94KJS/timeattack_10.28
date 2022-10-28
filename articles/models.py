from django.db import models
from django.contrib.auth.models import AbstractUser

class usermodel(AbstractUser):
    pass


class Article(models.Model):
    author = models.ForeignKey(usermodel, )
    title = models.CharField()
    content = models.TextField()