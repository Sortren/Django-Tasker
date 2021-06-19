from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


def validate_rating(value):
    if value < 0 or value > 100:
        raise ValidationError(
            ('Rating must be a number between 0 and 100'),
            params={'value': value},
        )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_tasks_finished = models.IntegerField(default=0)
    finished_before_deadline = models.IntegerField(default=0)
    finished_after_deadline = models.IntegerField(default=0)
    rating = models.IntegerField(default=0, validators=[validate_rating])

    def __str__(self):
        return self.user.username
