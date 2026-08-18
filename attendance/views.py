from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Attendance
from .forms import AttendanceForm
from students.models import Student


# =========================================================
# ROLE CHECK FUNCTIONS
# =========================================================

def get_role(request):
    if (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
    ):
        return request.user.userprofile.role

    return ""


def is_principal(request):
    return get_role(request) == "Principal"


def is_hod(request):
    return get_role(request) == "HOD"


def is_faculty(request):
    return get_role(request) == "Faculty"


def is_student(request):
    return get_role(request) == "Student"


# =========================================================
# ATTENDANCE LIST
# =========================================================

@login_required
def attendance_list(request):

    search = request.GET.get("search", "").strip()

    # =====================================================
    # PRINCIPAL / HOD / FACULTY
    # =====================================================

    if (
        is_principal(request)
        or is_hod(request)
        or is_faculty(request)
    ):

        attendance = Attendance.objects.all().order_by(
            "-attendance_date",
            "-id"
        )

        if search:

            attendance = attendance.filter(
                student__first_name__icontains=search
            ) | attendance.filter(
                student__last_name__icontains=search
            ) | attendance.filter(
                student__enrollment_no__icontains=search
            )

            attendance = attendance.order_by(
                "-attendance_date",
                "-id"
            )

    # =====================================================
    # STUDENT
    # =====================================================

    elif is_student(request):

        # Student login par saari attendance dikhayenge
        attendance = Attendance.objects.all().order_by(
            "-attendance_date",
            "-id"
        )

    # =====================================================
    # UNKNOWN USER
    # =====================================================

    else:

        return redirect("login")


    # =====================================================
    # PAGINATION
    # =====================================================

    paginator = Paginator(
        attendance,
        5
    )

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(
        page_number
    )


    # =====================================================
    # TEMPLATE
    # =====================================================

    return render(
        request,
        "attendance/attendance_list.html",
        {
            "attendance": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


# =========================================================
# ADD ATTENDANCE
# =========================================================

@login_required
def add_attendance(request):

    if not (
        is_principal(request)
        or is_hod(request)
        or is_faculty(request)
    ):

        return redirect("attendance_list")


    if request.method == "POST":

        form = AttendanceForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "attendance_list"
            )

    else:

        form = AttendanceForm()


    return render(
        request,
        "attendance/attendance_add.html",
        {
            "form": form
        }
    )


# =========================================================
# EDIT ATTENDANCE
# =========================================================

@login_required
def edit_attendance(request, id):

    if not (
        is_principal(request)
        or is_hod(request)
        or is_faculty(request)
    ):

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

            return redirect(
                "attendance_list"
            )

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


# =========================================================
# DELETE ATTENDANCE
# =========================================================

@login_required
def delete_attendance(request, id):

    if not (
        is_principal(request)
        or is_hod(request)
        or is_faculty(request)
    ):

        return redirect("attendance_list")


    attendance = get_object_or_404(
        Attendance,
        id=id
    )

    attendance.delete()

    return redirect(
        "attendance_list"
    )