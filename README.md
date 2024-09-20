# BookNest
BookNest is a Django-based book search web application that allows users to search for books using the Google Books API. Users can also bookmark their favorite books for future reference. The application features a clean and modern user interface built with Tailwind CSS, and it is responsive for both large and small screen devices.

## Table of Contents
- Features
- Tech Stack
- Installation
- Usage
- API Integration

## Features
- Search Books: Users can search for books by title, author, or keywords using the Google Books API.
- Bookmarks: Users can bookmark their favorite books and view them in a separate section.
- Responsive Design: The website is responsive and works well on both mobile and desktop devices.
- User-friendly Interface: Simple and intuitive navigation with a clean layout.

## Tech Stack
- Backend: Django
- Frontend: HTML, Tailwind CSS, JavaScript
- API: Google Books API
- Database: SQLite (default Django DB for development)

## Installation
### Prerequisites
- Python 3.x
- Django
- Git

### Steps
- Clone the repository:

```bash
  git clone https://github.com/Rohitthakan/BookSearchApp.git
  cd BookSearchApp
```
- Install dependencies:

```bash
  pip install -r requirements.txt
```
- Set up the database:

```bash
  python manage.py migrate
```
- Run the development server:

```bash
  python manage.py runserver
```
#### Open your browser and go to http://127.0.0.1:8000/.

## Usage
- Search for Books: Use the search bar on the homepage to find books.
- Bookmark Books: Click the bookmark button next to any book to save it for later.
- View Bookmarks: Navigate to the Bookmarks page to view saved books.

## API Integration
BookNest integrates with the Google Books API to fetch real-time book data based on user search queries. The API provides access to millions of books, offering details like title, author, publication date, and more.