from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):

        return self.content  # TODO: cut off