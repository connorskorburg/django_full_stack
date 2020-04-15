from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:num1>/', views.display),
    path('', views.shows),
    path('<int:num1>/update', views.update),
    path('<int:num1>/edit', views.edit),
    path('<int:num1>/destroy', views.destroy)
]