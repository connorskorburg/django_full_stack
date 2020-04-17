from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('destroy/<int:id>', views.destroy),
    path('delete/<int:id>', views.delete)
]