from django.db import models

class Writer(models.Model):
    witer_name = models.CharField(max_length=200)
    date_birth= models.DateTimeField('date published')

