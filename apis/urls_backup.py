from django.urls import path

from apis.views import (
    BookListAPIView, BookDetailAPIView,
    )

urlpatterns = [
    path("books/", BookListAPIView.as_view(), name="apis_book_list"),
    path("books/<int:pk>/", BookDetailAPIView.as_view(), name="apis_book_detail"),
]