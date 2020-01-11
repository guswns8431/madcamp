from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Blog
from .models import Love
from .models import Politics
from .models import Incident
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

def love(request):
    loves = Love.objects
    loves_list = Love.objects.all()
    paginator = Paginator(loves_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'love.html',{'loves' : loves,'posts':posts})

def politics(request):
    politics = Politics.objects
    politics_list = Politics.objects.all()
    paginator = Paginator(politics_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'politics.html',{'politics' : politics,'posts' : posts})

def incident(request):
    incidents = Incident.objects
    incidents_list = Incident.objects.all()
    paginator = Paginator(incidents_list,8)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'incident.html',{'incidents':incidents,'posts':posts})

def create(request):
    tmp = request.POST['category']
    if(tmp == '1'):
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.password = request.POST['password']
        blog.save()
        return redirect('board')
    elif(tmp == '2'):
        love = Love()
        love.title = request.POST['title']
        love.body = request.POST['body']
        love.pub_date = timezone.datetime.now()
        love.password = request.POST['password']
        love.save()
        return redirect('love')
    elif(tmp == '3'):
        politics = Politics()
        politics.title = request.POST['title']
        politics.body = request.POST['body']
        politics.pub_date = timezone.datetime.now()
        politics.password = request.POST['password']
        politics.save()
        return redirect('politics')
    else:
        incident = Incident()
        incident.title = request.POST['title']
        incident.body = request.POST['body']
        incident.pub_date = timezone.datetime.now()
        incident.password = request.POST['password']
        incident.save()
        return redirect('incident')



    #예준이 코드 혹시 몰라서 주석처리
    #blog = Blog()
    #blog.title = request.POST['title']
    #blog.body = request.POST['body']
    #blog.pub_date = timezone.datetime.now()
    #blog.password = request.POST['password']
    #blog.save()
    #return redirect('home')

def index(request):
    user = User.get.objects()
    return render(request,'home.html',{'User' : user})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog,pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def love_detail(request,love_id):
    love_detail = get_object_or_404(Love,pk = love_id)
    return render(request,'love_detail.html',{'love':love_detail})

def incident_detail(request,incident_id):
    incident_detail = get_object_or_404(Incident,pk = incident_id)
    return render(request,'incident_detail.html',{'incident':incident_detail})

def politics_detail(request,politics_id):
    politics_detail = get_object_or_404(Politics,pk = politics_id)
    return render(request,'politics_detail.html',{'politics':politics_detail})

