from django.shortcuts import render , redirect ,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from books.models import Book
from authors.models import Author


# def home(request):
#     books=Book.objects.all()
#     return render(request,'books/books.html', context={'books':books})

# def allbooks(request):
#     books=Book.objects.all()
#     return render(request, 'books/books.html',context={'books': books})

def index(request):
    books=Book.objects.all()
    return render(request,'books/index.html',context={'books':books})

def contactus(request):
    return render(request,'books/contactus.html')

def aboutus(request):
    return render(request,'books/aboutus.html')


def show(request, id ):
    book = get_object_or_404(Book, id=id)
    return render(request,'books/showdb.html',
                  context={'book': book})

def delete(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    url = reverse('books.index')
    return redirect(url)

def create(request):
    authors=Author.objects.all()
    if request.method == 'POST':
        book=Book()
        book.name=request.POST['name']
        book.price=request.POST['price']
        book.no_of_pages=request.POST['no_of_pages']
        # book.author=request.POST['author']
        # book.image=request.FILES['image']
        if 'author' in request.POST:
            author=Author.objects.filter(id=request.POST['author']).first() 
            if(author):
                book.author=author

        if 'image' in request.FILES:
            book.image = request.FILES['image']
        book.save()
        return redirect(book.show_url)
    
    return render(request, 'books/create.html',context={'authors':authors})
def edit(request, id):
    
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.name = request.POST['name']

        if 'no_of_pages' in request.POST:
            if request.POST['no_of_pages']!='':
                book.no_of_pages = request.POST['no_of_pages']
        if 'price' in request.POST:
            if request.POST['price']!='':
                book.no_of_pages = request.POST['price']
        
        if 'image' in request.FILES:
            book.image=request.FILES['image']
            
        if 'author' in request.POST:
            author=Author.objects.filter(name=request.POST['author']).first()
            if(author):
                book.author=author
        book.save()
        return redirect('books.index')
    
    return render(request, 'books/edit.html',
                  context={'book': book})