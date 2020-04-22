from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('books/', views.books),
    path('logout', views.logout),
    path('add_book', views.add_book),
    path('books/<int:book_id>', views.show_book,),
    path('update', views.update),
    path('add_fav_book', views.add_fav_book),
    path('remove_fav_book', views.remove_fav_book)
]