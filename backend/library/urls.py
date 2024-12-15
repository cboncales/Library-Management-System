from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet, BorrowedBookViewSet, ActivityLogViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('users', UserViewSet)
router.register('borrow_records', BorrowedBookViewSet)
router.register('activity_log', ActivityLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
