from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Department
from .forms import DepartmentForm


def principal_only(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "Principal"
    )


# Department List
@login_required
def department_list(request):

    if not principal_only(request):
        return redirect("login")

    search = request.GET.get("search", "")

    departments = Department.objects.all().order_by("id")

    if search:
        departments = departments.filter(
            department_name__icontains=search
        ) | Department.objects.filter(
            department_code__icontains=search
        ) | Department.objects.filter(
            hod_name__icontains=search
        )

    paginator = Paginator(departments, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


# Add Department
@login_required
def add_department(request):

    if not principal_only(request):
        return redirect("login")

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:
        form = DepartmentForm()

    return render(
        request,
        "departments/department_add.html",
        {
            "form": form
        }
    )


# Edit Department
@login_required
def edit_department(request, id):

    if not principal_only(request):
        return redirect("login")

    department = get_object_or_404(Department, id=id)

    if request.method == "POST":

        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:
        form = DepartmentForm(instance=department)

    return render(
        request,
        "departments/department_update.html",
        {
            "form": form
        }
    )


# Delete Department
@login_required
def delete_department(request, id):

    if not principal_only(request):
        return redirect("login")

    department = get_object_or_404(Department, id=id)

    department.delete()

    return redirect("department_list")