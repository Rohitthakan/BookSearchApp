from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_books, name='search_books'),
    path('bookmarks/', views.bookmarks, name='bookmarks'),
    path('add_bookmark/', views.add_bookmark, name='add_bookmark'),
    path('bookmark/<int:book_id>/', views.bookmark_book, name='bookmark_book'),
    path('remove_bookmark/<int:book_id>/', views.remove_bookmark, name='remove_bookmark'),
]
