from django.shortcuts import render, HttpResponse, redirect

from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "books" : Book.objects.all()
    }
    return render(request, 'index.html', context)

def create_book(request):
    Book.objects.create(
    title = request.POST['title'],
    description = request.POST['description'],
    )
    return redirect('/')

def books(request, book_id):
    context = {
        "authors" : Author.objects.all(),
        "book" : Book.objects.get(id=book_id),
    }
    book = Book.objects.get(id=1)
    print(book)
    return render(request, 'books.html', context)

def create_author(request):
    Author.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    notes = request.POST['notes'],
    )
    return redirect('/authors')

def list_authors(request):
    context = {
        "authors" : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def author(request, author_id):
    context = {
        "author" : Author.objects.get(id=author_id),
        "books" : Book.objects.all()
    }
    return render(request, 'author.html', context)

def add_author(request, book_id):
    author_id = request.POST['author_id']
    Book.objects.get(id=book_id).authors.add(author_id)
    return redirect('book_detail', book_id=book_id)

def add_book(request, author_id):
    book_id = request.POST['book_id']
    Author.objects.get(id=author_id).books.add(book_id)
    return redirect('author_detail', author_id=author_id)