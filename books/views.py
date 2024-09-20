from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Book, Bookmark
from django.contrib import messages
from django.urls import reverse 

def search_books(request):
    query = request.GET.get('q')
    page_number = request.GET.get('page', 1)

    try:
        page = int(page_number) if page_number else 1
    except ValueError:
        page = 1

    items_per_page = 3
    books = []
    previous_page = None
    next_page = None

    if query:
        url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
        response = requests.get(url)
        data = response.json()
        
        if 'items' in data:
            for item in data['items']:
                book_info = item['volumeInfo']
                books.append({
                    'id': item['id'],  
                    'title': book_info.get('title', 'N/A'),
                    'author': ', '.join(book_info.get('authors', [])),
                    'description': book_info.get('description', 'No description available')
                })
    
    total_books = len(books)
    if total_books > items_per_page:
        start_index = (page - 1) * items_per_page
        end_index = start_index + items_per_page
        books = books[start_index:end_index]

        if page > 1:
            previous_page = page - 1
        if end_index < total_books:
            next_page = page + 1

    return render(request, 'search.html', {
        'books': books,
        'query': query,
        'previous_page': previous_page,
        'next_page': next_page
    })

@login_required
def bookmarks(request):
    page = int(request.GET.get('page', 1))
    items_per_page = 3
    bookmarked_books = Bookmark.objects.filter(user=request.user)
    total_books = bookmarked_books.count()
    
    if total_books > items_per_page:
        start_index = (page - 1) * items_per_page
        end_index = start_index + items_per_page
        bookmarked_books = bookmarked_books[start_index:end_index]

        previous_page = page - 1 if page > 1 else None
        next_page = page + 1 if end_index < total_books else None
    else:
        previous_page = None
        next_page = None

    return render(request, 'bookmarks.html', {
        'bookmarked_books': bookmarked_books,
        'previous_page': previous_page,
        'next_page': next_page
    })

@login_required
@csrf_exempt 
def add_bookmark(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        
        Bookmark.objects.create(user=request.user, title=title, author=author, description=description)
        
        messages.success(request, 'Book added to bookmarks successfully.')

        query = request.POST.get('query', '')
        page = request.POST.get('page', 1)

        return redirect(f"{reverse('search_books')}?q={query}&page={page}")

    return redirect('search_books')


@login_required
def remove_bookmark(request, book_id):
    bookmark = get_object_or_404(Bookmark, id=book_id, user=request.user)
    bookmark.delete()
    return redirect('bookmarks')

@login_required
def bookmark_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    Bookmark.objects.get_or_create(user=request.user, book=book)

    return redirect('search_books') 
