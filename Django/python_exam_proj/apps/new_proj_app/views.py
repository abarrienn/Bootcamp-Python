from django.shortcuts import render, redirect
from django.contrib import messages
from .models import userManager, User
from .models import quoteManager, Quote

import bcrypt


def index(request):
    return render(request,'new_proj_app/index.html')

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
		'all_quotes' : Quote.objects.all()
		}
	return render(request, 'new_proj_app/first_page.html', context)

def logout(request):
	request.session.flush()
	request.session.clear()
	return redirect('/')

def process_quote(request):
	if request.method == "POST":
		errors = Quote.objects.basic_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)#make sure this error is not plural
			return redirect('/success')
		else:
			Quote.objects.create(author= request.POST['author'], quote= request.POST['quote'], creator= User.objects.get(id = request.session['logged_in']))
			return redirect('/success')
def destroy(request, id):
	if request.method == "POST":
		this_quote = Quote.objects.get(id=id)
		this_quote.delete()
		return redirect("/success")
	return redirect("/success")

def my_quotes(request, id):
	context = {
		'user': User.objects.get(id=request.session['logged_in']),
		'all_quotes': Quote.objects.all(),
		}
	return render(request, 'new_proj_app/view_quotes.html', context)
def edit(request, id):

	context = {
		'user': User.objects.get(id=request.session['logged_in']),
	}
	return render(request, 'new_proj_app/edit.html', context)
def update(request,id):
	if request.method == "POST":
		errors = User.objects.update_validator(request.POST)
		if len(errors) > 0:
			for key, value in errors.items():
				messages.error(request, value)#make sure this error is not plural
			return redirect('/edit')
		else:
			user_to_update = User.objects.get(id=id)
			user_to_update.first_name = request.POST['fname']
			user_to_update.last_name = request.POST['lname']
			user_to_update.email = request.POST['email']
			user_to_update.save()
			return redirect('/success')
