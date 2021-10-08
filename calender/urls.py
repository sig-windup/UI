from django.urls import path

from .views import calender_views

# 앱 마다 명칭 다르게 하기
app_name = 'calender'

urlpatterns = [

    # calender_views.py
    path('calender/list/', calender_views.calender_list, name='calender_list'),
]
