from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
    # registration validator
    def reg_validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 3:
            errors['first_name'] = "Please Enter a First Name with at least 2 characters!"
        if len(post_data['last_name']) < 3:
            errors['last_name'] = "Please Enter a Last Name with at least 2 characters!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Please Enter a valid Email Address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Please Enter a Password with at least 8 characters!"
        return errors
    # login validator
    def log_validator(self, post_data):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Please Enter a valid Email Address!"
        if len(post_data['password']) < 8:
            errors['password'] = "Please Enter a Password with at least 8 characters!"
        return errors
        
        
        
class BookManager(models.Manager):
    def book_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 1 or post_data['title'] == '':
            errors['title'] = "Please Enter a Title"
        if len(post_data['desc']) < 5:
            errors['desc'] = "Please Enter a Description with at least 5 characters!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)    
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # liked_books = a list of books a certain user likes
    # books_uploaded = a list of books uploaded by a certain user
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
        # the user who uploaded a certain book
    user_who_like = models.ManyToManyField(User, related_name="liked_books")
        # a list of users who like a given book
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()