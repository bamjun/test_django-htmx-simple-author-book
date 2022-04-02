from math import fabs
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Author, Book
from .forms import BookForm, AuthorForm

# Create your views here.


def author(request):
    author = Author.objects.all()

    context = {
        "author": author,
    }

    return render(request, "author/author.html", context)


def author_create(request):
    form = AuthorForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            author = form.save(commit=False)
            author.save()
            return redirect("author_detail", pk=author.id)

    context = {
        "form": form
    }
    return render(request, "author/author_create.html", context)


def author_detail(request, pk):
    form = Author.objects.get(pk=pk)
    context = {
        "form": form
    }
    return render(request, "author/author_detail.html", context)


def author_update(request, pk):
    author = Author.objects.get(pk=pk)
    form = AuthorForm(request.POST or None, instance=author)

    if request.method == 'POST':
        if form.is_valid():
            author = form.save()
            return redirect('author_detail', author.id)

    context = {
        "author": author,
        "form": form
    }
    return render(request, "author/author_create.html", context)


def author_delete(request, pk):
    form = Author.objects.get(pk=pk)
    form.delete()
    return HttpResponse('')


def book(request, pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)

    context = {
        "author": author,
        "books": books

    }

    return render(request, "book/book.html", context)


def book_create(request, pk):
    author = Author.objects.get(pk=pk)
    bookform = BookForm(request.POST or None)

    if request.method == 'POST':
        if bookform.is_valid():
            form = bookform.save(commit=False)
            form.author = author
            form.save()
            return redirect('book_detail', pk=form.id)

    context = {
        "author": author,
        "bookform": bookform,
    }

    return render(request, "book/book_create.html", context)


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book
    }
    return render(request, "book/book_detail.html", context)


def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    bookform = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if bookform.is_valid():
            book = bookform.save()
            return redirect('book_detail', pk=book.id)

    context = {
        'book': book,
        'bookform': bookform
    }

    return render(request, "book/book_create.html", context)


def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')
