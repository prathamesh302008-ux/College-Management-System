from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Book
from .forms import BookForm


# ==========================================================
# ROLE FUNCTIONS
# ==========================================================

def get_role(request):
    if request.user.is_authenticated and hasattr(request.user, "userprofile"):
        return request.user.userprofile.role
    return ""


def can_manage_library(request):
    return get_role(request) in [
        "Principal",
        "HOD",
        "Faculty",
    ]


def can_view_library(request):
    return get_role(request) in [
        "Principal",
        "HOD",
        "Faculty",
        "Student",
    ]


# ==========================================================
# BOOK LIST
# ==========================================================

@login_required
def book_list(request):

    if not can_view_library(request):
        return redirect("login")

    # Search
    search = request.GET.get("search", "").strip()

    books = Book.objects.all().order_by("id")

    if search:
        books = books.filter(
            book_name__icontains=search
        ) | books.filter(
            author__icontains=search
        ) | books.filter(
            book_code__icontains=search
        )

    # ======================================================
    # PAGINATION
    # ======================================================

    paginator = Paginator(books, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    # ======================================================
    # TEMPLATE
    # ======================================================

    return render(
        request,
        "library/book_list.html",
        {
            "books": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


# ==========================================================
# ADD BOOK
# ==========================================================

@login_required
def add_book(request):

    if not can_manage_library(request):
        return redirect("login")

    if request.method == "POST":

        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("book_list")

    else:
        form = BookForm()

    return render(
        request,
        "library/book_add.html",
        {
            "form": form
        }
    )


# ==========================================================
# UPDATE BOOK
# ==========================================================

@login_required
def edit_book(request, id):

    if not can_manage_library(request):
        return redirect("login")

    book = get_object_or_404(Book, id=id)

    if request.method == "POST":

        form = BookForm(
            request.POST,
            instance=book
        )

        if form.is_valid():
            form.save()
            return redirect("book_list")

    else:
        form = BookForm(instance=book)

    return render(
        request,
        "library/book_update.html",
        {
            "form": form
        }
    )


# ==========================================================
# DELETE BOOK
# ==========================================================

@login_required
def delete_book(request, id):

    if not can_manage_library(request):
        return redirect("login")

    book = get_object_or_404(Book, id=id)

    book.delete()

    return redirect("book_list")