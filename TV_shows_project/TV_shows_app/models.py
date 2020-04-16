from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Title should have at least 2 characters!"
        if len(post_data['network_name']) < 3:
            errors['network_name'] = "Network should have at least 3 Characters!"
        if len(post_data['desc']) < 9:
            errors['desc'] = "Description should have at least 10 characters!"
        if len(post_data['release_date']) < 1:
            errors['release_date'] = "Please enter a valid Release Date!"
        return errors

class Network(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
