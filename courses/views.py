from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Course
from .forms import CourseForm


def principal_only(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "Principal"
    )


# Course List
@login_required
def course_list(request):

    if not principal_only(request):
        return redirect("login")

    search = request.GET.get("search", "")

    courses = Course.objects.all().order_by("id")

    if search:
        courses = courses.filter(
            course_name__icontains=search
        ) | Course.objects.filter(
            course_code__icontains=search
        )

    paginator = Paginator(courses, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "courses/course_list.html",
        {
            "courses": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


# Add Course
@login_required
def add_course(request):

    if not principal_only(request):
        return redirect("login")

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm()

    return render(
        request,
        "courses/course_add.html",
        {
            "form": form
        }
    )


# Edit Course
@login_required
def edit_course(request, id):

    if not principal_only(request):
        return redirect("login")

    course = get_object_or_404(Course, id=id)

    if request.method == "POST":

        form = CourseForm(
            request.POST,
            instance=course
        )

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseForm(instance=course)

    return render(
        request,
        "courses/course_update.html",
        {
            "form": form
        }
    )


# Delete Course
@login_required
def delete_course(request, id):

    if not principal_only(request):
        return redirect("login")

    course = get_object_or_404(Course, id=id)

    course.delete()

    return redirect("course_list")