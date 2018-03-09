from django.shortcuts import render
from django.views import generic
from .models import Book



def book_view(request):
    model=Book

    book_list = Book.objects.all()
    context = {
        "temp": book_list
    }
    return render(request, 'Book_List.html', context)

def book_detail(req,pk):
    book_item = Book.objects.get(pk=pk)
    context = {
        "temp": book_item
    }
    return render(req, 'book_Detail.html', context)