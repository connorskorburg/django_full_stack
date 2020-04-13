from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('<int:num1>', views.display),
]