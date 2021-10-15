from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article


def article_list(request):
    """
    article 출력
    """
    team_text = request.GET.get('team')
    print(team_text)
    if(team_text != '전체' and team_text != None):
        article_list = Article.objects.filter(article_team=team_text)
    else:
        article_list = Article.objects.order_by('-written_time')
    context = {
        'team_text': team_text,
        'article_list': article_list,
     }

    return render(request, 'article/article_list.html', context)