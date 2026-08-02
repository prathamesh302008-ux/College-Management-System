from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Attendance
from .forms import AttendanceForm
from students.models import Student


def is_principal(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "Principal"
    )


def is_hod(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "HOD"
    )


def is_faculty(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "Faculty"
    )


def is_student(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "Student"
    )


@login_required
def attendance_list(request):

    search = request.GET.get("search", "")

    # ==========================
    # Principal / HOD / Faculty
    # ==========================

    if is_principal(request) or is_hod(request) or is_faculty(request):

        attendance = Attendance.objects.all().order_by("-attendance_date")

        if search:

            attendance = attendance.filter(
                student__first_name__icontains=search
            ) | Attendance.objects.filter(
                student__last_name__icontains=search
            )

    # ==========================
    # Student
    # ==========================

    elif is_student(request):

        try:

            student = Student.objects.get(
                user=request.user
            )

            attendance = Attendance.objects.filter(
                student=student
            ).order_by("-attendance_date")

        except Student.DoesNotExist:

            attendance = Attendance.objects.none()

    else:

        return redirect("login")

    paginator = Paginator(attendance, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "attendance/attendance_list.html",
        {
            "attendance": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


@login_required
def add_attendance(request):

    if not (is_principal(request) or is_hod(request) or is_faculty(request)):
        return redirect("attendance_list")

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("attendance_list")

    else:

        form = AttendanceForm()

    return render(
        request,
        "attendance/attendance_add.html",
        {
            "form": form
        }
    )


@login_required
def edit_attendance(request, id):

    if not (is_principal(request) or is_hod(request) or is_faculty(request)):
        return redirect("attendance_list")

    attendance = get_object_or_404(
        Attendance,
        id=id
    )

    if request.method == "POST":

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():

            form.save()

            return redirect("attendance_list")

    else:

        form = AttendanceForm(
            instance=attendance
        )

    return render(
        request,
        "attendance/attendance_update.html",
        {
            "form": form
        }
    )


@login_required
def delete_attendance(request, id):

    if not (is_principal(request) or is_hod(request) or is_faculty(request)):
        return redirect("attendance_list")

    attendance = get_object_or_404(
        Attendance,
        id=id
    )

    attendance.delete()

    return redirect("attendance_list")