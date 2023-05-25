from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)
    author = models.CharField(max_length=40)
    data = models.DateField(default=timezone.now)
