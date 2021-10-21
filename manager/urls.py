from django.urls import path

from .views import manager_views

# 앱 마다 명칭 다르게 하기
app_name = 'manager'

urlpatterns = [
    # article_views.py
    path('list/', manager_views.article_list, name='article_list'),
    path('<int:article_id>/',manager_views.reinforce, name='reinforce'),
]
