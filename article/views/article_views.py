from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from article.models import Article
# from ..forms import PostForm

# 일정에 대하여 다시하기
def article_list(request):
    """
    article 출력
    """
    article_list = Article.objects.order_by('-written_time')
    context = {'article_list': article_list}
    return render(request, 'article/article_list.html', context)