from django.contrib import admin
from .models import Books, SwapRequest


# Register your models here.
@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'condition', 'available', 'owner')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre', 'condition', 'available')


@admin.register(SwapRequest)
class SwapRequestAdmin(admin.ModelAdmin):
    list_display = ('requester', 'book', 'book_author', 'book_genre', 'timestamp')
    search_fields = (
        'requester__username',
        'book__title',
        'book__author',
        'book__genre',
    )
    list_filter = (
        'book__genre',
        'book__condition',
        'book__available',
    )

    def book_author(self, obj):
        return obj.book.author
    book_author.short_description = 'Author'

    def book_genre(self, obj):
        return obj.book.genre
    book_genre.short_description = 'Genre'


