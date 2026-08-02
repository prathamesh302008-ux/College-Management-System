from django import forms

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = "__all__"

        widgets = {

            "book_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "book_code": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "author": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "publisher": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "available": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "status": forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),

        }