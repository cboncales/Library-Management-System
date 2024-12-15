from rest_framework import serializers
from .models import Book, User, BorrowedBook, ActivityLog

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BorrowedBookSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    book = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = BorrowedBook
        fields = '__all__'

class ActivityLogSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ActivityLog
        fields = '__all__'
