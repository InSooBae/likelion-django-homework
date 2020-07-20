from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost
# Create your views here.


def home(request):
    # * 모델로부터 객체 목록을 받음 -> 쿼리셋 /(메소드)
    # * 쿼리셋 , 메소드 형식 -> 모델.쿼리셋{Object}.메소드()
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs, 'posts': posts})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})


def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))


def blogpost(request):
    #  입력된 내용을 처리하는 기능 (POST)
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    #  빈 페이지를 띄워주는 기능 (GET)
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form': form})


def search(request):
    blogs = Blog.objects.all().order_by('-id')

    ser = request.POST.get('search', "")

    if ser:
        blogs = blogs.filter(title__icontains=ser)
        return render(request, 'res.html', {'blogs': blogs, 'search': ser})

    else:
        return render(request, 'res.html')
