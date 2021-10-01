from django.shortcuts import render, get_object_or_404


def index(request):
    """
    windup 목록 출력
    """
    return render(request, 'windup/home.html')
