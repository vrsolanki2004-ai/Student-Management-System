from django.urls import path
from .views import (
    StudentListCreateView,
    StudentRetrieveUpdateDeleteView,
    RegisterView,
)

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentRetrieveUpdateDeleteView.as_view(), name='student-detail'),

    path('register/', RegisterView.as_view(), name='register'),
]