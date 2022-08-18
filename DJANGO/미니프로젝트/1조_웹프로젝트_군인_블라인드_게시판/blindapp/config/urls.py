"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import login, views as auth_views
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/' , views.register),
    path('register2/', views.register2 , name = 'register2'),   
    path('login/',views.login),
    path('send_mail/',views.send_mail),
    path('check_code/',views.check_code),

    path('accountinformation/',views.accountinfo),
    path('settings/',views.setting),
    path('logout/',views.logout),
    path('myload/',views.myload),
    path('myloadmore/',views.myloadmore),
    path('deleteid/',views.deleteid),
    path('deleteconf/',views.deleteconf),
    path('mybookload/',views.mybookload),

    path('load/', views.load),
    path('load2/', views.load2),
    path('load3/', views.load3),
    path('load4/', views.load4),
    path('comingsoon/',views.comingsoon),

    path('loadmore/', views.load_more),
    path('loadmore2/', views.load_more2),
    path('loadmore3/', views.load_more3),
    path('loadmore4/', views.load_more4),

    path('loadsearch/', views.load_search),
    path('loadsearch2/', views.load_search2),
    path('loadsearch3/', views.load_search3),
    path('loadsearch4/', views.load_search4),
    
    path('loadsearchmy/', views.load_searchmy),
    path('loadsearchbookmark/',views.loadsearchbookmark),

    path('posting/', views.posting), #gabby
    path('posting4/', views.posting4),
    path('noticeposting/', views.posting3), # 공지사항 작성

    path('like/', views.like),
    path('replylisting/', views.replylisting), #gabby
    path('replyposting/', views.postreply), #gabby
    


    path('bookmark/', views.bookmark),
    path('mybookmark/',views.mybookmark),
    path('mybookmarkmore/', views.mybookmarkmore),

    path('clear/',views.clear),
    path('checkid/', views.checkid),
    path('deleteposting/', views.deleteposting),
    path('updatepost/',views.updatepost),
    path('updatereply/', views.updatereply),
    path('deletereply/', views.deletereply),


    path('upload/', views.upload_image),



]
