from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Faculty
from .forms import FacultyForm


def principal_only(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "Principal"
    )


# Faculty List
@login_required
def faculty_list(request):

    if not principal_only(request):
        return redirect("login")

    search = request.GET.get("search", "")

    faculty = Faculty.objects.all().order_by("id")

    if search:
        faculty = faculty.filter(
            first_name__icontains=search
        ) | Faculty.objects.filter(
            last_name__icontains=search
        ) | Faculty.objects.filter(
            faculty_id__icontains=search
        )

    paginator = Paginator(faculty, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "faculty/faculty_list.html",
        {
            "faculty": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


# Add Faculty
@login_required
def add_faculty(request):

    if not principal_only(request):
        return redirect("login")

    if request.method == "POST":

        form = FacultyForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("faculty_list")

    else:
        form = FacultyForm()

    return render(
        request,
        "faculty/faculty_add.html",
        {
            "form": form
        }
    )


# Edit Faculty
@login_required
def edit_faculty(request, id):

    if not principal_only(request):
        return redirect("login")

    faculty = get_object_or_404(Faculty, id=id)

    if request.method == "POST":

        form = FacultyForm(
            request.POST,
            request.FILES,
            instance=faculty
        )

        if form.is_valid():
            form.save()
            return redirect("faculty_list")

    else:
        form = FacultyForm(instance=faculty)

    return render(
        request,
        "faculty/faculty_update.html",
        {
            "form": form
        }
    )


# Delete Faculty
@login_required
def delete_faculty(request, id):

    if not principal_only(request):
        return redirect("login")

    faculty = get_object_or_404(Faculty, id=id)

    faculty.delete()

    return redirect("faculty_list")