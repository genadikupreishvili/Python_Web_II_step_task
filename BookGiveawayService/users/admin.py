from django.contrib import admin
from .models import Book, Author, Genre, Condition
from .forms import BookForm

class BookAdmin(admin.ModelAdmin):
    form = BookForm


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Condition)
