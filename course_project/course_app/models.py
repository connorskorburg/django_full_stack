from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def course_validator(self, post_data):
        errors = {}

        if len(post_data['course_name']) < 7:
            errors['course_name'] = "Course Name should be at least 6 characters!"
        if len(post_data['desc']) < 16:
            errors['desc'] = "Description should be 16 at least characters!"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()