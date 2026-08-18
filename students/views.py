from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Student
from .forms import StudentForm


# =====================================================
# ROLE
# =====================================================

def get_role(request):

    if hasattr(request.user, "userprofile"):
        return request.user.userprofile.role

    return ""


def is_student(request):

    return get_role(request) == "Student"


def can_manage_students(request):

    return get_role(request) in [
        "Principal",
        "HOD",
        "Faculty",
    ]


# =====================================================
# STUDENT LIST
# =====================================================

@login_required
def student_list(request):

    # =================================================
    # PRINCIPAL / HOD / FACULTY
    # =================================================

    if can_manage_students(request):

        search = request.GET.get(
            "search",
            ""
        )

        students = Student.objects.all().order_by("id")

        if search:

            students = students.filter(
                first_name__icontains=search
            ) | students.filter(
                last_name__icontains=search
            ) | students.filter(
                enrollment_no__icontains=search
            )

        # 5 students per page
        paginator = Paginator(
            students,
            5
        )

        page_number = request.GET.get(
            "page"
        )

        page_obj = paginator.get_page(
            page_number
        )

        return render(
            request,
            "students/student_list.html",
            {
                "students": page_obj,
                "page_obj": page_obj,
                "search": search,
                "principal": True,
            }
        )

    # =================================================
    # STUDENT
    # =================================================

    elif is_student(request):

        try:

            student = Student.objects.get(
                user=request.user
            )

        except Student.DoesNotExist:

            return render(
                request,
                "students/student_list.html",
                {
                    "students": [],
                    "page_obj": [],
                    "search": "",
                    "principal": False,
                    "message": "Student record not found.",
                }
            )

        return render(
            request,
            "students/student_list.html",
            {
                "students": [student],
                "page_obj": [student],
                "search": "",
                "principal": False,
            }
        )

    # =================================================
    # ACCESS DENIED
    # =================================================

    return HttpResponseForbidden(
        "Access Denied"
    )


# =====================================================
# ADD STUDENT
# =====================================================

@login_required
def add_student(request):

    if not can_manage_students(request):

        return HttpResponseForbidden(
            "Access Denied"
        )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect(
                "student_list"
            )

    else:

        form = StudentForm()

    return render(
        request,
        "students/student_add.html",
        {
            "form": form
        }
    )


# =====================================================
# EDIT STUDENT
# =====================================================

@login_required
def edit_student(request, id):

    if not can_manage_students(request):

        return HttpResponseForbidden(
            "Access Denied"
        )

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():

            form.save()

            return redirect(
                "student_list"
            )

    else:

        form = StudentForm(
            instance=student
        )

    return render(
        request,
        "students/student_update.html",
        {
            "form": form
        }
    )


# =====================================================
# DELETE STUDENT
# =====================================================

@login_required
def delete_student(request, id):

    if not can_manage_students(request):

        return HttpResponseForbidden(
            "Access Denied"
        )

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect(
        "student_list"
    )