from django.urls import path

from apis import views


urlpatterns = [
    path("books/", views.books, name="books_list"),
    path("books/<int:id>/", views.book_detail, name="book_detail"),
]