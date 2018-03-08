from django.shortcuts import render

# Create your views here.
#views.py
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext



#Hossam Login & Register

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
            request.session['username'] = user['username']
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

"""
#sessionLogin
 username = request.session['username']

        return render_to_response(
            'home.html',
            {'user': request.user}
        )
        
     if request.session.has_key('username'):
        return render(request, 'home.html',{'user': request.user})
    else:
        return render(request, 'login.html', {})
"""