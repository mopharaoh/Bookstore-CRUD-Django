from django.urls import path
from authors.views import index,show,AuthorCreate,AuthorDelete,AuthorEdit,AuthorShow
urlpatterns = [
    
    # path('home/',home_author),
    path('authors/', index, name='authors.index'),
    path('<int:author_id>',show,name='authors.show'),
    path('createat', AuthorCreate.as_view(), name='authors.createat'),
    path('<int:pk>/delete', AuthorDelete.as_view(), name='authors.delete'),
    path('<int:pk>/edit', AuthorEdit.as_view(), name='authors.edit'),
    # path('index/<int:pk>', AuthorShow.as_view(), name='authors.show'),
]