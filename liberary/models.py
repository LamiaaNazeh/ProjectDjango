from django.db import models
from django.urls import reverse







class Writer(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    bio=models.TextField(blank=True)
    contact = models.CharField(max_length=100, null=True)
    image=models.ImageField(upload_to="picture/",blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)
class Meta:
    ordering = ["first_name" , "last_name"]
def get_absolute_url(self):
    return reverse('author-detail', args=[str(self.id)])



class Book(models.Model):
    title = models.CharField(max_length=200)
    date_publish= models.DateTimeField(default='')
    sammary=models.TextField(blank=True)
    country= models.TextField(blank=True)
    link = models.URLField(blank=True)
    Writer = models.ForeignKey(Writer,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.title

    class Meta:
        ordering =['title']
