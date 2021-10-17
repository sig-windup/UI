from django.contrib import admin
from django.db import models

class Article(models.Model):
    #현재 주석처리 된 건 추후에 추가예정
    #현재 모델간의 연관관계가 없기에 int로 박아넣음
    article_team = models.CharField(max_length=20)
    article_title = models.TextField()
    written_time = models.DateField()
    #article_content = models.TextField()
    #article_url = models.TextField()
    #keyword = models.TextField()

