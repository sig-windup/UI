from django.urls import path
from .views import base_views

# 앱 마다 명칭 다르게 하기
app_name = 'home'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
]
