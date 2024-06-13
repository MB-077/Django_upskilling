from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import *
from django.http import Http404

def index(request):
    books = Book.objects.all()
    return render(request, 'book_outlet/index.html', {'books': books})

# def book_detail(request, id):
def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404('Book not found')
    # book = get_object_or_404(Book, pk=id)
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title,
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestseller,
        })