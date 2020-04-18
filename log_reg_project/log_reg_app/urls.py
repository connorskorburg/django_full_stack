from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('wall', views.wall),
    path('login', views.login),
    path('logout', views.logout),
    path('add_message', views.add_message),
    path('add_comment', views.add_comment)
]