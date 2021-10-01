from django.db import models

class Post(models.Model):
    writer = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    team = models.TextField()
    date = models.DateTimeField()

