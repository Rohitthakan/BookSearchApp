from django.contrib import admin
from books.models import Book, Bookmark

# Register your models here.
admin.site.register(Book)
admin.site.register(Bookmark)