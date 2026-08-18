from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Notice
from .forms import NoticeForm


def get_role(request):
    if request.user.is_authenticated and hasattr(request.user, "userprofile"):
        return request.user.userprofile.role
    return ""


def can_manage_notice(request):
    return get_role(request) in [
        "Principal",
        "HOD",
        "Faculty",
    ]


def can_view_notice(request):
    return get_role(request) in [
        "Principal",
        "HOD",
        "Faculty",
        "Student",
    ]


# Notice List
@login_required
def notice_list(request):

    if not can_view_notice(request):
        return redirect("login")

    search = request.GET.get("search", "")

    notices = Notice.objects.all().order_by("-id")

    if search:
        notices = notices.filter(
            title__icontains=search
        )

    paginator = Paginator(notices, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "noticeboard/notice_list.html",
        {
            "notices": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


# Add Notice
@login_required
def add_notice(request):

    if not can_manage_notice(request):
        return redirect("login")

    if request.method == "POST":

        form = NoticeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("notice_list")

    else:

        form = NoticeForm()

    return render(
        request,
        "noticeboard/notice_add.html",
        {
            "form": form
        }
    )


# Edit Notice
@login_required
def edit_notice(request, id):

    if not can_manage_notice(request):
        return redirect("login")

    notice = get_object_or_404(Notice, id=id)

    if request.method == "POST":

        form = NoticeForm(
            request.POST,
            instance=notice
        )

        if form.is_valid():
            form.save()
            return redirect("notice_list")

    else:

        form = NoticeForm(instance=notice)

    return render(
        request,
        "noticeboard/notice_update.html",
        {
            "form": form
        }
    )


# Delete Notice
@login_required
def delete_notice(request, id):

    if not can_manage_notice(request):
        return redirect("login")

    notice = get_object_or_404(Notice, id=id)

    notice.delete()

    return redirect("notice_list")