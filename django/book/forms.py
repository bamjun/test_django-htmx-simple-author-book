from dataclasses import field
from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = (
            "name",
        )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "number_of_pages",
        )
