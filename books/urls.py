from django.urls import path

from .views import (BookListView, BookDetailView, 
                    BookDeleteView, BookAddView,
                    BookUpdateView, SearchBookListView,
                    books_add_from_file
                    )

urlpatterns = [
    path("", BookListView.as_view(), name="books"),
    path("search/", SearchBookListView.as_view(), name="books_search"),
    path("add/", BookAddView.as_view(), name="book_add"),
    path("add-from-file/", books_add_from_file, name="books_add_from_file"),
    path("<int:pk>/", BookDetailView.as_view(), name="book_details"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="book_update"),
]