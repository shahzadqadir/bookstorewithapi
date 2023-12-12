import json
from books.models import Book, Author
from django.http import JsonResponse, QueryDict
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

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
def book_detail(request, id):
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
        book.delete()
        return JsonResponse({"message":"book deleted successfully."})