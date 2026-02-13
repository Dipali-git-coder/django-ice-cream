from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name=''),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup')
]