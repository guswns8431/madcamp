from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:    
                user = User.objects.create_user(
                request.POST['email'], password = request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        return render(request,'signup.html')