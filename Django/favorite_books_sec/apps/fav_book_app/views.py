from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userManager, User
from .models import bookManager, Book
import bcrypt


def index(request):
    return render(request,'fav_book_app/index.html')

def register(request):
	if request.method=="POST":
		errors = User.objects.reg_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)#make sure this error is not plural
			return redirect('/')
		else:
			hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
			User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email=request.POST['email'], password=hashedpw)
			user = User.objects.last()
			request.session['logged_in'] = user.id
			return redirect('/success')
		return redirect('/')

def login(request):
	if request.method=="POST":
		errors = User.objects.login_validate(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)#make sure this error is not plural
			return redirect('/')
		else:
			user = User.objects.get(email=request.POST['email'])
			request.session['logged_in'] = user.id
			return redirect('/success')
		
		return redirect('/')
def success(request):
	if User.objects.get(id=request.session['logged_in']) == User.objects.last():
		status = "registered"
	else:
		status = "logged in"

	context = {
		'user': User.objects.get(id=request.session['logged_in']),
		'status': status,
		'all_books' : Book.objects.all()
		}
	return render(request, 'fav_book_app/first_page.html', context)

def logout(request):
	request.session.flush()
	request.session.clear()
	return redirect('/')
def add_book(request):
	if request.method == "POST":
		errors = Book.objects.basic_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)#make sure this error is not plural
			return redirect('/add_book')
		else:
			favd_books = Book.objects.create(title= request.POST['title'], description= request.POST['description'], creator= User.objects.get(id = request.session['logged_in']))
			favd_books.users_who_liked.add(request.session['logged_in'])
			return redirect('/success')
