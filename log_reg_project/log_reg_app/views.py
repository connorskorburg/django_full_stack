from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

# handling Render templates
def index(request):
    return render(request, 'index.html')

def success(request):
    if 'user' not in request.session:
        return redirect('/')
    return render(request, 'success.html')

# handling POST data
def register(request):
    errors = User.objects.user_validator(request.POST)

    if len(errors) > 0:
        
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')

    if request.POST['pass'] == request.POST['conf_pass']:
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['pass'])
        return redirect('/success')
    else:
        return redirect('/')

def login(request):
    email = request.POST['email']
    logged_user = User.objects.filter(email=email)
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pass']:
            request.session['user'] = logged_user.first_name
            return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')