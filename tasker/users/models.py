from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_tasks_finished = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
