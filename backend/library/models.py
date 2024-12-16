from django.db import models
from django.utils import timezone
from decimal import Decimal
from django.db import connection
import uuid

# Create your models here.

class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Cataloger', 'Cataloger'),
    ]

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    year_published = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now) 
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title


class BorrowedBook(models.Model):
    borrow_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField()
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} borrowed {self.book.title}"


class ActivityLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action_type = models.CharField(max_length=50) 
    table_name = models.CharField(max_length=50)  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        if self.user:
            return f"{self.action_type} on {self.table_name} by {self.user.first_name} {self.user.last_name}"
        return f"{self.action_type} on {self.table_name} by Unknown"

class BorrowedBooksSummary(models.Model):
    user_id = models.UUIDField()
    username = models.CharField(max_length=100)
    total_books_borrowed = models.PositiveIntegerField()

    class Meta:
        managed = False  # Prevent Django from managing the database
        db_table = 'borrowed_books_by_the_user'  # Name of the view


class OverdueBooks(models.Model):
    borrow_id = models.UUIDField()
    borrower = models.CharField(max_length=100)
    book_title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)
    overdue_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'overdue_books'

class MonthlyBorrowingTrends(models.Model):
    month = models.DateField()
    total_borrowed = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'monthly_borrowing_trends'


def refresh_materialized_view():
    with connection.cursor() as cursor:
        cursor.execute('REFRESH MATERIALIZED VIEW monthly_borrowing_trends')
