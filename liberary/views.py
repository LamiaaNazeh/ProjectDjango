from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from .models import Writer
from .models import Book
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext




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


@csrf_protect


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
         #   request.session['username'] = user['username']
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

    """
    context ={
        'form': form
    }

    return render_to_response(
    'registration/register.html',
    context,
    )
    """

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect('registration/logout.html')

 
@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})
    else:
        return render(request, 'login.html', {})


