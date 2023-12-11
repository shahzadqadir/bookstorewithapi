from csv import reader as csv_reader

from .models import Book, Author


def search_define_author(author_name):
    authors = Author.objects.filter(name__iexact=author_name)
    if len(authors) <= 0:
        return Author.objects.create(name=author_name)        
    return authors[0]


def search_book(book_name):
    return len(Book.objects.filter(title__iexact=book_name)) > 0


def import_books_from_file(filename):
    list_of_books = []
    with open(filename) as file:
        reader = csv_reader(file)
        next(reader)
        for row in reader:
            if not search_book(row[0]):
                book = Book(title=row[0],
                    author=search_define_author(row[1]),
                    price=float(row[2])
                )
                list_of_books.append(book)
    return list_of_books

