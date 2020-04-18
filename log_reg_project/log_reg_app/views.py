from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

# handling Render templates
def index(request):
    return render(request, 'index.html')

def wall(request):
    if 'user_first_name' not in request.session:
        return redirect('/')
    else:
        comments = Comment.objects.all()
        messages = Message.objects.all()
        context = {
            'messages': messages,
            'comments': comments,
        }
        return render(request, 'wall.html', context)
    
# handling POST data
# registering a user
def register(request):
    errors = User.objects.user_validator(request.POST)

    if len(errors) > 0:
        
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')

    if request.POST['pass'] == request.POST['conf_pass']:
        new_user = User.objects.create(first_name = request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['pass'])
        request.session['user_first_name'] = new_user.first_name
        request.session['user_last_name'] = new_user.last_name
        request.session['user_email'] = new_user.email
        request.session['user_id'] = new_user.id
        return redirect('/wall')
    else:
        return redirect('/')

# logging in and out 
# login
def login(request):
    email = request.POST['email']
    logged_user = User.objects.filter(email=email)
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if logged_user.password == request.POST['pass']:
            request.session['user_first_name'] = logged_user.first_name
            request.session['user_last_name'] = logged_user.last_name
            request.session['user_email'] = logged_user.email
            request.session['user_id'] = logged_user.id
            return redirect('/wall')
    return redirect('/')
# logout
def logout(request):
    request.session.flush()
    return redirect('/')

# adding a message
def add_message(request):
    id = int(request.session['user_id'])
    user = User.objects.get(id=id)
    message = Message.objects.create(content=request.POST['message'], user=user)
    return redirect('/wall')

# adding a comment to a message
def add_comment(request):
    id = int(request.session['user_id'])
    user = User.objects.get(id=id)
    message_id = int(request.POST['message_id'])
    message = Message.objects.filter(id=message_id)
    # print(message[0])
    # print(user)
    # print(request.POST)
    # print(request.POST['comment'])
    comment = Comment.objects.create(user=user,message=message[0],content=request.POST['comment'])
    return redirect('/wall')