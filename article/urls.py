from django.urls import path

from . import article_views

# 앱 마다 명칭 다르게 하기
app_name = 'article'

urlpatterns = [
    # article_views.py
    path('list/', article_views.article_list, name='article_list'),
]
