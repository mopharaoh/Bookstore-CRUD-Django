from django.shortcuts import render , get_object_or_404 ,redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.views import View
# Create your views here.
from authors.models import Author
from authors.forms import AuthorForm



# def home_author(request):
#     return render(request, 'authors/home.html')


def index(request):
    authors = Author.objects.all()
    return render(request, 'authors/index.html',
                  context={'authors': authors})

def show(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'authors/show.html',
                  context={'author': author})


# class TrackCreate(View):
#     # get request ?
#     def get(self, request, *args, **kwargs):
#         # return with create form
#         form = AuthorForm()
#         return render(request, 'authors/create.html',
#                       {'form': form})

#     # post request
#     def post(self, request, *args, **kwargs):
#         form = AuthorForm(request.POST, request.FILES)
#         if form.is_valid():
#             track = form.save()
#             return redirect(author.show_url)


class AuthorCreate(CreateView):
    
    form_class = AuthorForm
    template_name = 'authors/createat.html'
    success_url = '/authors/index/{id}'


class AuthorDelete(DeleteView):

    template_name = 'authors/delete.html'
    success_url = '/authors/authors'
    model=Author

class AuthorEdit(UpdateView):
    form_class=AuthorForm
    template_name='authors/edit.html'
    success_url='/authors/authors'
    model=Author

class AuthorShow(DetailView):

    template_name='authors/show.html'
    model=Author
    context_object_name='auhtor'
