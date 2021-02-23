from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('book/create', views.create_book),
    path('books/<int:book_id>', views.books, name="book_detail"),
    path('book/<int:book_id>/author/add', views.add_author, name="add_author"),
    path('authors/create', views.create_author),
    path('authors', views.list_authors),
    path('authors/<int:author_id>', views.author, name="author_detail"),
    path('author/<int:author_id>/book/add', views.add_book, name="add_book")
]