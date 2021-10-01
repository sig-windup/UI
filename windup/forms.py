from django import forms
from windup.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # 사용할 모델
        fields = ['title','writer','content']  # PostForm에서 사용할 Post 모델의 속성
        labels = {
            'title': '제목',
            'writer': '작성자',
            'content': '내용',
        }