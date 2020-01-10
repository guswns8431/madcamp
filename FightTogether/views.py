from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Blog
# Create your views here.


def home(request):
    return render(request,'home.html')

def board(request):
    blogs = Blog.objects
    return render(request,'board.html',{'blogs' : blogs})

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
