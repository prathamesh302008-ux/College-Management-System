from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from students.models import Student
from faculty.models import Faculty
from courses.models import Course
from departments.models import Department
from attendance.models import Attendance
from fees.models import Fee
from library.models import Book
from noticeboard.models import Notice


@login_required
def dashboard_view(request):

    role = request.user.userprofile.role

    context = {
        "role": role,
        "username": request.user.username,
    }

    # =========================
    # PRINCIPAL
    # =========================

    if role == "Principal":

        context.update({

            "total_students": Student.objects.count(),

            "total_faculty": Faculty.objects.count(),

            "total_courses": Course.objects.count(),

            "total_departments": Department.objects.count(),

            "total_attendance": Attendance.objects.count(),

            "total_fees": Fee.objects.count(),

            "total_books": Book.objects.count(),

            "total_notices": Notice.objects.count(),

            "latest_students": Student.objects.order_by("-id")[:5],

            "latest_faculty": Faculty.objects.order_by("-id")[:5],

            "latest_notices": Notice.objects.order_by("-id")[:5],

        })


    # =========================
    # STUDENT
    # =========================

    elif role == "Student":

        try:

            student = Student.objects.get(
                user=request.user
            )
            attendance = Attendance.objects.filter(
                student=student
            )

            fee = Fee.objects.filter(
                student=student
            ).first()

            context.update({

                "student": student,

                "attendance_count": attendance.count(),

                "present_count": attendance.filter(
                    status="Present"
                ).count(),

                "absent_count": attendance.filter(
                    status="Absent"
                ).count(),

                "leave_count": attendance.filter(
                    status="Leave"
                ).count(),

                "fee": fee,

                "books": Book.objects.count(),

                "latest_notices": Notice.objects.order_by("-id")[:5],

            })

        except Student.DoesNotExist:

            context["student"] = None


    # =========================
    # HOD
    # =========================

    elif role == "HOD":

        context.update({

            "total_attendance": Attendance.objects.count(),

            "total_books": Book.objects.count(),

            "latest_notices": Notice.objects.order_by("-id")[:5],

        })


    # =========================
    # FACULTY
    # =========================

    elif role == "Faculty":

        context.update({

            "total_attendance": Attendance.objects.count(),

            "total_books": Book.objects.count(),

            "latest_notices": Notice.objects.order_by("-id")[:5],

        })

    return render(
        request,
        "dashboard/home.html",
        context
    )