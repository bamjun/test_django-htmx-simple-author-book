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
    form = BookForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("book", pk=book.id)

    context = {
        "author": author,
        "form": form
    }

    return render(request, "book/book.html", context)


def book_create(request):
    return HttpResponse('')


def book_detail(request):
    return HttpResponse('')


def book_update(request):
    return HttpResponse('')


def book_delete(request):
    return HttpResponse('')
