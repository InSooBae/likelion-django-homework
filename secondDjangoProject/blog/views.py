from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def home(request):
    # * 모델로부터 객체 목록을 받음 -> 쿼리셋 /(메소드)
    # * 쿼리셋 , 메소드 형식 -> 모델.쿼리셋{Object}.메소드()
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})
