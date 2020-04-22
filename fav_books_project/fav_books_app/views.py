from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


# template methods

# display home page with login and register
def index(request):
    return render(request, 'index.html')
# display page with add book and list of all books
def books(request):
    if 'first_name' not in request.session:
        return redirect('/')
    else:
        all_books = Book.objects.all()
        user = User.objects.get(id=request.session['id'])
        liked_books = user.liked_books.all()
        context = {
            'all_books': all_books,
            'liked_books': liked_books,
        }
        return render(request, 'books.html', context)

# display a certain book
def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    users_who_like = book.user_who_like.all()
    context = {
        'book': book,
        'users_who_like': users_who_like,
    }
    return render(request, 'show_book.html', context)



# POST methods

# register user
def register(request):
    # check for valid user data
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    # if passwords match hash and salt password for security
    if request.POST['password'] == request.POST['conf_password']:
        password = request.POST['password']
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        # create new user 
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password_hash)
        request.session['id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        request.session['last_name'] = new_user.last_name
        request.session['email'] = new_user.email
        return redirect('/books')
    return redirect('/')
# login
def login(request):
    # check for valid user data
    errors = User.objects.log_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/')
    # check for user
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            request.session['first_name'] = logged_user.first_name
            request.session['last_name'] = logged_user.last_name
            request.session['email'] = logged_user.email
            return redirect('/books')
    return redirect('/')
# logout
def logout(request):
    request.session.flush()
    return redirect('/')
# add a new book
def add_book(request):
    # get user that wants to add book
    id = int(request.session['id'])
    user = User.objects.get(id=id)
    # create new book
    new_book = Book.objects.create(title=request.POST['title'], desc=request.POST['desc'], uploaded_by=user)
    # add the user to liked books
    new_book.user_who_like.add(user)
    return redirect('/books')

# update or delete a book if user in session
def update(request):
    print(request.POST)
    if 'update' in request.POST:
        book = Book.objects.get(id=int(request.POST['update']))
        if request.session['id'] == book.uploaded_by.id:
            book.title = request.POST['title']
            book.desc = request.POST['desc']
            book.save()

    if 'delete' in  request.POST:
        book = Book.objects.get(id=int(request.POST['delete']))
        if request.session['id'] == book.uploaded_by.id:
            book.delete()
    return redirect('/books')

def add_fav_book(request):
    pass