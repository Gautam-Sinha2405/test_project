from django.urls import path
from library import views

urlpatterns= [
    path('createbook/', views.create_book, name='createbook'),
    path('createAuthor/', views.create_author, name='createAuthor'),
    path('get_book_by_id/<int:book_id>', views.get_book_by_id, name='get_book_by_id'),
    path('get_author_by_id/<int:author_id>', views.get_author_by_id, name='get_author_by_id'),
]