
from django.contrib import admin
from django.urls import path
from liberary import  views

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


