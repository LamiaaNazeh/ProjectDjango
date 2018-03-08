from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Writer
from .models import Book



def book_view(request):


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
#######################################################################
##writer



def index(request):
    num_authors = Writer.objects.all()

    return render(
        request,
        'liberary/List_Writers.html',
        {'num_authors': num_authors},
    )


def Writer_view(request, pk):
    model = Writer

    Writer_list = Writer.objects.get(pk=pk)
    Writer_book= Writer.objects.get(id=pk)

    context = {
        "temp": Writer_list,
        "temp2":Writer_book.book_set.all()

    }

    return render(
        request,
        'liberary/base_generic.html',
        context
    )


    return render(
        request,
        'liberary/base_generic.html',
        context
    )




