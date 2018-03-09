
from django.contrib import admin
from django.urls import path
from liberary import  views
from django.conf.urls import url, include
from liberary.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('books/', views.book_view, name='books'),
    path('books/books/<int:pk>', views.book_detail, name='book-detail'),
    path('liberary/liberary/books/books/<int:pk>', views.book_detail, name='book-detail'),
    path('liberary/liberary/<int:pk>', views.Writer_view),
    path('<int:pk>', views.Writer_view),
    path('liberary/', views.index, name='index'),

]
urlpatterns += [
    path('', include('django.contrib.auth.urls')),
    path('', home),
    path('/', home),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', home),
    path('register/', register),
    path('register/success/', register_success),
    path('logout/', include('django.contrib.auth.urls')),
]
