
from django.conf.urls import patterns, url
from notification import views

urlpatterns = patterns('',
        url(r'^$', views.user_login, name='login'),
        url(r'^dashboard/', views.home, name='home'),
        url(r'^logout/', views.user_logout, name='logout'),
        )