from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    ListView, DetailView, 
    DeleteView, CreateView,
    UpdateView
    )
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book, Author
from .forms import BulkBookAdditionForm
from books import helper_functions as hf

class BookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/book_list.html"


class SearchBookListView(ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/search_book_list.html"

    def get_queryset(self):
        if self.request.GET.get("q") == "all":
            return Book.objects.all()
        return Book.objects.filter(Q(title__icontains=self.request.GET.get("q")) | 
                                   Q(author__name__icontains=self.request.GET.get("q")))

class BookDetailView(DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = "books/book_delete.html"
    success_url = reverse_lazy("homepage")


class BookAddView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "books/book_add.html"
    fields = "__all__"

    success_url = reverse_lazy("books")


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = "__all__"
    # success_url = Book.get_absolute_url()


# function based forms

@login_required
def books_add_from_file(request):
    form = BulkBookAdditionForm()
    print("this is only a test!")
    if request.method == "POST":
        filename = request.POST.get("filename")
        new_books = hf.import_books_from_file(filename)
        for book in new_books:
            Book.objects.create(
                title=book.title,
                author=book.author,
                price=book.price
            )
        return redirect(reverse_lazy("books"))

    return render(request, "books/books_from_file.html", {"form": form})