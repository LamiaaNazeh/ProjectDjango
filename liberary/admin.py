from django.contrib import admin
from .models import  Book
from .models import  Writer
#
#
#
admin.site.register(Book)
# admin.site.register(Writer)


# Register your models here.
#class WriterAdmin(admin.ModelAdmin):
    #list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death','contact')
    #fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Writer)
