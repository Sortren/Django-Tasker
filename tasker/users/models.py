from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_tasks_finished = models.IntegerField(default=0)
    finished_before_deadline = models.IntegerField(default=0)
    finished_after_deadline = models.IntegerField(default=0)
    rating = models.IntegerField(default=0, validators=[
                                 MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.user.username
