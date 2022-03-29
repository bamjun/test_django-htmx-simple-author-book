from django.urls import path
from . import views

urlpatterns = [
    path('', views.author, name='author'),
    path('htmx/author_create/', views.author_create, name='author_create'),
    path('htmx/author_detail/<pk>/', views.author_detail, name='author_detail'),
    path('htmx/author_delete/<pk>/', views.author_delete, name='author_delete'),
    path('htmx/author_update/<pk>/', views.author_update, name='author_update'),
    path('<int:pk>/', views.book, name='book'),
    path('htmx/book_create/', views.book_create, name='book_create'),
    path('htmx/book_detail/<pk>/', views.book_detail, name='book_detail'),
    path('htmx/book_update/<pk>/', views.book_update, name='book_update'),
    path('htmx/book_delete/<pk>/', views.book_delete, name='book_delete'),
]
