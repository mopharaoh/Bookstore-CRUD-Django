from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='authors/images',null=True,blank=True)
    bdate=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def show_url(self):
        url = reverse('authors.show', args=[self.id])
        return url
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def edit_url(self):
        url = reverse('authors.edit', args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse('authors.delete', args=[self.id])
        return url