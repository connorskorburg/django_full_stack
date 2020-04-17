from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

# render templates
def index(request):
    all_courses = Course.objects.all()
    context = {
        'all_courses': all_courses,
    }
    return render(request, 'index.html', context)

def destroy(request, id):
    current_course = Course.objects.get(id=id)
    context = {
        'current_course': current_course,
    }
    return render(request, 'destroy.html', context)

# handling POST data
def new(request):
    errors = Course.objects.course_validator(request.POST)
    # check if there are any validation errors
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    # create a new course if it passes validation
    new_course = Course.objects.create(name=request.POST['course_name'], desc=request.POST['desc'])
    return redirect('/')

def delete(request, id):
    # determine if the user choose the 'Yes I want to delete this' button
    if 'remove' in request.POST:
        delete_course = Course.objects.get(id=id)
        delete_course.delete()
    return redirect('/')

