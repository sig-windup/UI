from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article
from datetime import datetime, timedelta
from django.utils.dateformat import DateFormat

def date_range():
    today = DateFormat(datetime.now()).format('ymd')
    start = datetime.strptime(today, "%y%m%d") - timedelta(days=4)
    dates = [(start + timedelta(days=i)).strftime("20%y-%m-%d") for i in range(5)]
    return dates

def article_list(request):
    """
    article 출력
    """
    team_text = request.GET.get('team','')
    date = request.GET.get('date')
    dates = date_range()

    #dates[4] = 현재 날짜
    if(team_text != '전체' and team_text != None):
        article_list = Article.objects.filter(article_team=team_text, written_time=dates[4])
    elif(date == None):
        article_list = Article.objects.filter(written_time=dates[4])
    else:
        article_list = Article.objects.filter(written_time=date)

    context = {
        'team_text': team_text,
        'article_list': article_list,
        'dates': dates,
     }

    return render(request, 'article/article_list.html', context)