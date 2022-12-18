from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class WeeklyTasks(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    taskname = models.CharField(max_length=200, default=None)