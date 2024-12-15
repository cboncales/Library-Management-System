from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book, User, BorrowedBook, ActivityLog
from .serializers import BookSerializer, UserSerializer, BorrowedBookSerializer, ActivityLogSerializer
from .utils import calculate_fine, get_user_borrowed_books

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BorrowedBookViewSet(ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer

class ActivityLogViewSet(ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

def fine_calculation_view(request):
    due_date = request.GET.get('due_date')  # Example: '2024-12-01'
    returned_date = request.GET.get('returned_date')  # Example: '2024-12-10'
    
    if due_date and returned_date:
        fine = calculate_fine(due_date, returned_date)
    else:
        fine = "Invalid input"

    return render(request, 'library/fine_result.html', {'fine': fine})

def user_borrowed_books_view(request, user_id):
    borrowed_books = get_user_borrowed_books(user_id)
    return render(request, 'library/borrowed_books.html', {'borrowed_books': borrowed_books})