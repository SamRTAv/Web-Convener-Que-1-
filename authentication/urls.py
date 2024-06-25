from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import render_pdf_view
from allauth.account.views import logout

urlpatterns = [
    path('', views.home,name = "home"),
    path('signin',views.signin,name = "signin"),
    path('signup',views.signup,name = "signup"),
    path('signout',views.signout,name = "signout"), 
    path('bookDrive',views.bookDrive,name = 'test-view'),
    path('upload',views.upload,name = 'upload'),
    path('google',views.google,name = 'google sign in'),
    path('viewfile',views.viewfile,name = 'check'),
    path('logout/', logout, name='socialaccount_logout'),
    # path('list',views.list,name = "list")
]