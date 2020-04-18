from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        # first name validation
        if len(post_data['first_name']) < 3:
            errors['first_name'] = "Please enter a first name with more than 2 characters!"
        if post_data['first_name'].isalpha() == False:
            errors['first_name'] = "Please enter a first name with alphabetic characters!"
        # last name validation
        if len(post_data['last_name']) < 3:
            errors['last_name'] = "Please enter a last name with more than 2 characters!"
        if post_data['last_name'].isalpha() == False:
            errors['last_name'] = "Please enter a last name with alphabetic characters!"
        # password validation
        if len(post_data['pass']) < 8:
            errors['pass'] = "Please enter a password with at least 8 characters!"
        if post_data['pass'] != post_data['conf_pass']:
            errors['pass'] = "Please make sure you confirmed the right password!"
        # email validation
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):            
            errors['email'] = ("Invalid email address!")

        return errors

        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Message(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)