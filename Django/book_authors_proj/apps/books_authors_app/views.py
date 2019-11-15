from django.shortcuts import render, redirect
from .models import Book
from .models import Author

def index(request):
	context = {
		"all_books" : Book.objects.all()
	}
	print(context)
	return render(request,'books_authors_app/index.html', context)

def add_book(request):
	if request.method == 'POST':
		new_book = Book.objects.create(title = request.POST['title'], desc = request.POST['description'])
		print(new_book)
	return redirect('/')

def view_book(request, id):
	context = {
		"book" : Book.objects.get(id=id),
		"all_authors": Author.objects.all()
	}
	return render(request, 'books_authors_app/view_book.html', context)
def add_auth_to_list(request, id):
	if request.method == "POST":
		this_author = Author.objects.get(id= id)
		this_list = Author.books.all()
		this_list.add(this_author)
		print(this_list)
		return redirect('/view_book'+ str(id))

def author_template(request):
	context = {
		"all_authors" : Author.objects.all()
	}
	return render(request, 'books_authors_app/add_author.html', context)
def view_author(request, id):
	
		context = {
			"author" : Author.objects.get(id=id),
			"all_books": Book.objects.all(),
		}
		return render(request,'books_authors_app/view_author.html', context)
def add_book_to_list(request, id):
	if request.method == "POST":
		this_book = Book.authors.get(id= id)
		this_list = Authors.authors.all()
		this_list.add(this_book)
		print(this_list)
		return redirect('/view_author')

