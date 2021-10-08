from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from calender.models import Calender
# from ..forms import PostForm

# 일정에 대하여 다시하기
def calender_list(request):
    """
    post 일정 출력
    """
    calender_list = Calender.objects.order_by('date')
    context = {'calender': calender_list}
    return render(request, 'calender/calender.html', context)
