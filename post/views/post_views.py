from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Post
from ..forms import PostForm
from django.contrib import messages

def post_list(request):
    """
    post 목록 출력
    """
    post_list = Post.objects.order_by('-date')
    context = {'post_list': post_list}
    return render(request, 'post/post_list.html', context)

def post_create(request):
    """
    post 게시글등록
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('post:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post/post_form.html', context)

def post_detail(request, post_id):
    """
    post 내용 출력
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'post/post_detail.html', context)
