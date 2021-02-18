from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     title = models.CharField(max_length=85, )
     note = models.CharField(max_length=500)
     link = models.URLField(max_length=210)
     date = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.title
