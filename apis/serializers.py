from rest_framework import serializers

from books.models import Book, Author

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    author = AuthorSerializer()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
