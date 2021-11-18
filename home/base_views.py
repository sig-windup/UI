from django.shortcuts import render, get_object_or_404

from home.models import Matches, Teams


def index(request):
    #stategame이 없을 경우 게임예정이다 -> score, result 모두 에도 점수가 없다.

    matches = Matches.objects.filter(date="20210921")
    img = Teams.objects.all()

    context = {
        'matches': matches,
        'img': img,
     }
    return render(request, 'home/home.html', context)

