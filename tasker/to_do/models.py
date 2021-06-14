from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    class Priority(models.IntegerChoices):
        # ex. the user see LOW in the Form which represents "1" in a database
        LOW = 1
        MEDIUM = 2
        HIGH = 3

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    finished = models.BooleanField(default=False)
    updated = models.BooleanField(default=False)
    priority = models.IntegerField(default=1, choices=Priority.choices)
    deadline = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
