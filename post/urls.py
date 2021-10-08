from django.urls import path
from .views import post_views

# 앱 마다 명칭 다르게 하기
app_name = 'post'

urlpatterns = [
    # post_views.py
    path('post/list/',
         post_views.post_list, name='post_list'),
    path('post/create/',
         post_views.post_create, name='post_create'),
    path('<int:post_id>/',
         post_views.post_detail, name='post_detail'),

]
