
from django.urls import path
from books.views import contactus,aboutus,delete,show,index,create,edit
urlpatterns = [
    # path('b', allbooks, name='allbooks'),
    # path('books',home),
    path('contact',contactus),
    path('aboutus',aboutus),
    path('index',index,name='books.index'),
    path('index/<int:id>', show, name='books.show'),
    path('<int:id>/delete', delete, name='books.delete'),
    path('create',create,name='books.create'),
    path('<int:id>/edit',edit,name='books.edit')
]