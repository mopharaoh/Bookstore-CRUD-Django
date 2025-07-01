from django.db import models
from authors.models import Author
from django.urls import reverse
# Create your models here.


class Book(models.Model):

    name=models.CharField(max_length=100)
    no_of_pages=models.IntegerField(max_length=100)
    # author=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    image=models.ImageField(upload_to='books/images',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,
                            related_name='books',null=True,blank=True)


    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        return f'/media/{self.image}'

    @property
    def show_url(self):
        url = reverse('books.show', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('books.edit', args=[self.id])
        return url