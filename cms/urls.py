from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("admin/", admin.site.urls),

    # Website (Home Page)
    path("", include("website.urls")),

    # Login
    path("login/", include("accounts.urls")),

    # Dashboard
    path("dashboard/", include("dashboard.urls")),

    # Students
    path("students/", include("students.urls")),

    # Faculty
    path("faculty/", include("faculty.urls")),

    # Departments
    path("departments/", include("departments.urls")),

    # Courses
    path("courses/", include("courses.urls")),

    # Attendance
    path("attendance/", include("attendance.urls")),

    # Fees
    path("fees/", include("fees.urls")),

    # Library
    path("library/", include("library.urls")),

    # Notice Board
    path("noticeboard/", include("noticeboard.urls")),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )