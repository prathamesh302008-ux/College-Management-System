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


# =====================================================
# ANALYTICS PAGE
# =====================================================

@login_required
def analytics(request):

    role = request.user.userprofile.role

    context = {
        "role": role,
        "username": request.user.username,

        # =================================================
        # COLLEGE TOTALS
        # =================================================

        "total_students": Student.objects.count(),
        "total_faculty": Faculty.objects.count(),
        "total_courses": Course.objects.count(),
        "total_departments": Department.objects.count(),
        "total_attendance": Attendance.objects.count(),
        "total_fees": Fee.objects.count(),
        "total_books": Book.objects.count(),
        "total_notices": Notice.objects.count(),
    }

    # =====================================================
    # STUDENT ANALYTICS
    # =====================================================

    if role == "Student":

        try:
            student = Student.objects.get(
                user=request.user
            )

            attendance = Attendance.objects.filter(
                student=student
            )

            context.update({

                "student": student,

                "student_attendance":
                    attendance.count(),

                "student_present":
                    attendance.filter(
                        status="Present"
                    ).count(),

                "student_absent":
                    attendance.filter(
                        status="Absent"
                    ).count(),

                "student_leave":
                    attendance.filter(
                        status="Leave"
                    ).count(),

                "student_fee":
                    Fee.objects.filter(
                        student=student
                    ).first(),
            })

        except Student.DoesNotExist:

            context.update({
                "student": None,
                "student_attendance": 0,
                "student_present": 0,
                "student_absent": 0,
                "student_leave": 0,
                "student_fee": None,
            })

    return render(
        request,
        "dashboard/analytics.html",
        context
    )


# =====================================================
# DASHBOARD HOME
# =====================================================

@login_required
def home(request):

    role = request.user.userprofile.role

    context = {
        "role": role,
        "username": request.user.username,
    }


    # =================================================
    # PRINCIPAL
    # =================================================

    if role == "Principal":

        context.update({

            # -------------------------------
            # MAIN COUNTS
            # -------------------------------

            "total_students":
                Student.objects.count(),

            "total_faculty":
                Faculty.objects.count(),

            "total_courses":
                Course.objects.count(),

            "total_departments":
                Department.objects.count(),

            "total_attendance":
                Attendance.objects.count(),

            "total_fees":
                Fee.objects.count(),

            "total_books":
                Book.objects.count(),

            "total_notices":
                Notice.objects.count(),

            # -------------------------------
            # LATEST DATA
            # -------------------------------

            "latest_students":
                Student.objects.order_by("-id")[:5],

            "latest_faculty":
                Faculty.objects.order_by("-id")[:5],

            "latest_notices":
                Notice.objects.order_by("-id")[:5],
        })


    # =================================================
    # STUDENT
    # =================================================

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

                # -------------------------------
                # STUDENT INFORMATION
                # -------------------------------

                "student": student,

                # -------------------------------
                # OWN ATTENDANCE ONLY
                # -------------------------------

                "attendance_count":
                    attendance.count(),

                "present_count":
                    attendance.filter(
                        status="Present"
                    ).count(),

                "absent_count":
                    attendance.filter(
                        status="Absent"
                    ).count(),

                "leave_count":
                    attendance.filter(
                        status="Leave"
                    ).count(),

                # -------------------------------
                # OWN FEE
                # -------------------------------

                "fee": fee,

                # -------------------------------
                # LIBRARY
                # -------------------------------

                "books":
                    Book.objects.count(),

                # -------------------------------
                # NOTICES
                # -------------------------------

                "latest_notices":
                    Notice.objects.order_by("-id")[:5],
            })

        except Student.DoesNotExist:

            context.update({

                "student": None,

                "attendance_count": 0,

                "present_count": 0,

                "absent_count": 0,

                "leave_count": 0,

                "fee": None,

                "books":
                    Book.objects.count(),

                "latest_notices":
                    Notice.objects.order_by("-id")[:5],
            })


    # =================================================
    # HOD
    # =================================================

    elif role == "HOD":

        context.update({

            "total_attendance":
                Attendance.objects.count(),

            "total_books":
                Book.objects.count(),

            "total_notices":
                Notice.objects.count(),

            "latest_notices":
                Notice.objects.order_by("-id")[:5],
        })


    # =================================================
    # FACULTY
    # =================================================

    elif role == "Faculty":

        context.update({

            "total_attendance":
                Attendance.objects.count(),

            "total_books":
                Book.objects.count(),

            "total_notices":
                Notice.objects.count(),

            "latest_notices":
                Notice.objects.order_by("-id")[:5],
        })


    # =================================================
    # RENDER DASHBOARD
    # =================================================

    return render(
        request,
        "dashboard/home.html",
        context
    )