from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # =====================================================
    # ADMIN
    # =====================================================

    path(
        "admin/",
        admin.site.urls
    ),


    # =====================================================
    # WEBSITE
    # HOME / ABOUT / HELP / CONTACT
    # =====================================================

    path(
        "",
        include("website.urls")
    ),


    # =====================================================
    # ACCOUNTS
    # LOGIN / REGISTER / LOGOUT
    # =====================================================

    path(
        "login/",
        include("accounts.urls")
    ),


    # =====================================================
    # DASHBOARD
    # =====================================================

    path(
        "dashboard/",
        include("dashboard.urls")
    ),


    # =====================================================
    # STUDENTS
    # =====================================================

    path(
        "students/",
        include("students.urls")
    ),


    # =====================================================
    # FACULTY
    # =====================================================

    path(
        "faculty/",
        include("faculty.urls")
    ),


    # =====================================================
    # DEPARTMENTS
    # =====================================================

    path(
        "departments/",
        include("departments.urls")
    ),


    # =====================================================
    # COURSES
    # =====================================================

    path(
        "courses/",
        include("courses.urls")
    ),


    # =====================================================
    # ATTENDANCE
    # =====================================================

    path(
        "attendance/",
        include("attendance.urls")
    ),


    # =====================================================
    # FEES
    # =====================================================

    path(
        "fees/",
        include("fees.urls")
    ),


    # =====================================================
    # LIBRARY
    # =====================================================

    path(
        "library/",
        include("library.urls")
    ),


    # =====================================================
    # NOTICE BOARD
    # =====================================================

    path(
        "noticeboard/",
        include("noticeboard.urls")
    ),

]


# =========================================================
# MEDIA FILES
# =========================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )