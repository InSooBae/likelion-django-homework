from django.shortcuts import render
from .models import Blog
# Create your views here.


def home(request):
    # * 모델로부터 객체 목록을 받음 -> 쿼리셋 /(메소드)
    # * 쿼리셋 , 메소드 형식 -> 모델.쿼리셋{Object}.메소드()
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})
