from django.db import models

class Post(models.Model):
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    team = models.CharField(max_length=20)
    date = models.DateTimeField()
