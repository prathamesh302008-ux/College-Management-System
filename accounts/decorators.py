from django.shortcuts import redirect


def principal_required(view_func):

    def wrapper(request, *args, **kwargs):

        if (
            request.user.is_authenticated and
            request.user.userprofile.role == "Principal"
        ):
            return view_func(request, *args, **kwargs)

        return redirect("/dashboard/")

    return wrapper


def hod_required(view_func):

    def wrapper(request, *args, **kwargs):

        if (
            request.user.is_authenticated and
            request.user.userprofile.role == "HOD"
        ):
            return view_func(request, *args, **kwargs)

        return redirect("/dashboard/")

    return wrapper


def faculty_required(view_func):

    def wrapper(request, *args, **kwargs):

        if (
            request.user.is_authenticated and
            request.user.userprofile.role == "Faculty"
        ):
            return view_func(request, *args, **kwargs)

        return redirect("/dashboard/")

    return wrapper


def student_required(view_func):

    def wrapper(request, *args, **kwargs):

        if (
            request.user.is_authenticated and
            request.user.userprofile.role == "Student"
        ):
            return view_func(request, *args, **kwargs)

        return redirect("/dashboard/")

    return wrapper