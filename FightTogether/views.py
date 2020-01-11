from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Blog
from django.core.paginator import Paginator #페이지를 나누기 위해 선언
# Create your views here.


def home(request):
    return render(request,'home.html')

def index1(request): #맨처음 화면 띄워줌
    return render(request,'index1.html')

def board(request):
    blogs = Blog.objects
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 8 개를 한 페이지로 자르기
    paginator = Paginator(blog_list,8)
    #request된 페이지가 뭔지 알아낸다 (request페이지를 변수에 담는다)
    page = request.GET.get('page')
    #request되 페이지를 얻어온 뒤 return
    posts = paginator.get_page(page)
    return render(request,'board.html',{'blogs' : blogs,'posts':posts})

def newpost(request):
    return render(request,'newpost.html')

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.pub_date = timezone.datetime.now()
    blog.password = request.POST['password']
    blog.save()
    return redirect('home')

def index(request):
    user = User.get.objects()
    return render(request,'home.html',{'User' : user})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

