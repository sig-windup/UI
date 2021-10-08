from django.db import models

class Calender(models.Model):
    date = models.DateTimeField()
    home_team = models.CharField(max_length=20)
    away_team = models.CharField(max_length=20)
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    location = models.CharField(max_length=20)
