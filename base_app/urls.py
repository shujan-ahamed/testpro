from django.contrib import auth
from django.urls import path,include
from base_app import views


urlpatterns =[
    path('',views.index ,name='index'),
    path('register_page',views.register_page,name='register_page'),
    path('login_page',views.login_page,name='login'),
    path('logout_user',views.logoutUser,name='logout'),
    
    ]