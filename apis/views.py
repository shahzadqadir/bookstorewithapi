import json
from books.models import Book, Author
from django.http import JsonResponse, QueryDict
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from books import helper_functions as hf


@csrf_exempt
def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        books_dict_list = [model_to_dict(book) for book in books]
        for book in books_dict_list:
            book["author"] = model_to_dict(Author.objects.get(id=book["author"]))
        return JsonResponse({"data":books_dict_list})
    if request.method == "POST":
        new_book = json.loads(request.body)
        if len(Book.objects.filter(title=new_book["title"])) >= 1:
            return JsonResponse({"error": "book already exist."})
        book = Book.objects.create(
            title=new_book["title"],
            author=hf.search_define_author(new_book["author"]),
            price=new_book["price"]
        )
        return JsonResponse({"book_details":model_to_dict(book), "message": "book added successfully."})
        


@csrf_exempt
def book(request, id):
    try:
        book = Book.objects.get(id=id) 
    except Exception:
        return JsonResponse({"error": "book not found."})
    if request.method == "GET":
        book_dict = model_to_dict(book)
        book_dict["author"] = model_to_dict(Author.objects.get(id=book_dict["author"]))
        return JsonResponse({"data":book_dict})
    if request.method == "PUT":               
        new_book_detail = json.loads(request.body)
        book.title = new_book_detail["title"]
        book.author = Author.objects.get(id=new_book_detail["author"])
        book.price = new_book_detail["price"]
        book.save()
        return JsonResponse({"new_details": model_to_dict(book),"success":"book details updated"})
    if request.method == "DELETE":
        if request.user.is_staff or request.user.is_superuser:
            book.delete()
            return JsonResponse({"message": f"{book.title} deleted successfully."})
        return JsonResponse({"message":"User not authorized to perform this action."})
    

@csrf_exempt
def authors(request):
    if request.method == "GET":
        authors = Author.objects.all()
        authors_dicts = [model_to_dict(author) for author in authors]
        return JsonResponse({"data": authors_dicts})
    

@csrf_exempt
def author(request, id):
    try:
        author = Author.objects.get(id=id)
    except Exception:
        return JsonResponse({"error": "author not found."})
    if request.method == "GET":
        return JsonResponse({"data": model_to_dict(author)})
    if request.method == "PUT":
        new_author_details = json.loads(request.body)
        if len(new_author_details) < 2:
            return JsonResponse({"error": "both author name and email are required."})
        author.name = new_author_details["name"]
        author.email = new_author_details["email"]
        author.save()
        return JsonResponse({"new_author_details": model_to_dict(author), "success": "author details updated."})
    if request.method == "DELETE":
        if len(author.books.all()) > 0:
            return JsonResponse({"error": "can't delete, author has books added"})
        author.delete()
        return JsonResponse({"success", "author deleted successfully."}, safe=False)
    

def author_books(request, id):
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return JsonResponse({"error": "author not found."})
    author_books = author.books.all()
    author_books_dicts = [model_to_dict(book) for book in author_books]
    return JsonResponse({"data":author_books_dicts})