from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def board(request):
    return render(request,'board.html')

def newpost(request):
    return render(request,'newpost.html')