"""madcamp3stproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import login.views
import FightTogether.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',FightTogether.views.index1,name="index1"),
    path('login/',login.views.login,name="login"),
    path('signup/',login.views.signup,name="signup"),
    path('home/',FightTogether.views.home,name="home"),
    path('board/',FightTogether.views.board,name="board"),
    path('love/',FightTogether.views.love,name="love"),
    path('incident/',FightTogether.views.incident,name="incident"),
    path('politics/',FightTogether.views.politics,name="politics"),
    path('newpost/',FightTogether.views.newpost,name="newpost"),
    path('create/',FightTogether.views.create, name="create"),
    path('index/',FightTogether.views.index,name="index"),
    path('blog/<int:blog_id>',FightTogether.views.detail,name="detail"),
    path('love/<int:love_id>',FightTogether.views.love_detail,name="love_detail"),
    path('incident/<int:incident_id>',FightTogether.views.incident_detail,name="incident_detail"),
    path('politics/<int:politics_id>',FightTogether.views.politics_detail,name="politics_detail"),
    path('refute/',FightTogether.views.refute,name="refute"),
    path('blog/like/<int:blog_id>', FightTogether.views.post_like_toggle, name="post_like_toggle"),
    path('incident/like/<int:incident_id>', FightTogether.views.post_like_toggle1, name="post_like_toggle1"),
    path('love/like/<int:love_id>', FightTogether.views.post_like_toggle2, name="post_like_toggle2"),
    path('politics/like/<int:politics_id>', FightTogether.views.post_like_toggle3, name="post_like_toggle3"),
    path('refute/like/<int:refute_id>', FightTogether.views.post_like_toggle_refute, name="post_like_toggle_refute"),
    
]
