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

    """
    Author is a foreign key in a Task's table, because the containing user's id is being taken from the User's table 
    to create a relation between them. Now each task has a field called "author" filled with an id of the user
    who created this task. 
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
