from django.urls import path

from apis import views


urlpatterns = [
    path("books/", views.books, name="books"),
    path("books/<int:id>/", views.book, name="book"),
    path("authors/", views.authors, name="authors"),
    path("authors/<int:id>/", views.author, name="author"),
    path("authors/<int:id>/books/", views.author_books, name="author_books"),
]