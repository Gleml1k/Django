from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class User1(models.Model):

    username = models.CharField(max_length=40, blank=False, verbose_name='username')
    name = models.CharField(max_length=40, blank=False, verbose_name='name')
    password = models.CharField(max_length=100, blank=False, verbose_name='password')
    data_reg = models.DateField(auto_now_add=timezone.now)

    def __str__(self):
        return f'{self.username}'