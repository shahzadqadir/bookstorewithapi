from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_details", kwargs={"pk": self.pk})

