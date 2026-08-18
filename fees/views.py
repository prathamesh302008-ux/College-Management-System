from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Fee
from .forms import FeeForm
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


def is_student(request):
    return (
        request.user.is_authenticated
        and hasattr(request.user, "userprofile")
        and request.user.userprofile.role == "Student"
    )


@login_required
def fee_list(request):

    search = request.GET.get("search", "")

    # Principal & HOD
    if is_principal(request) or is_hod(request):

        fees = Fee.objects.all().order_by("-id")

        if search:
            fees = fees.filter(
                student__first_name__icontains=search
            ) | Fee.objects.filter(
                student__last_name__icontains=search
            )

    # Student
    elif is_student(request):

        try:
            student = Student.objects.get(user=request.user)

            fees = Fee.objects.filter(
                student=student
            ).order_by("-id")

        except Student.DoesNotExist:
            fees = Fee.objects.none()

    else:
        return redirect("login")

    paginator = Paginator(fees, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "fees/fee_list.html",
        {
            "fees": page_obj,
            "page_obj": page_obj,
            "search": search,
        }
    )


@login_required
def add_fee(request):

    # Principal + HOD
    if not (is_principal(request) or is_hod(request)):
        return redirect("fee_list")

    if request.method == "POST":

        form = FeeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("fee_list")

    else:

        form = FeeForm()

    return render(
        request,
        "fees/fee_add.html",
        {
            "form": form
        }
    )


@login_required
def edit_fee(request, id):

    # Principal + HOD
    if not (is_principal(request) or is_hod(request)):
        return redirect("fee_list")

    fee = get_object_or_404(
        Fee,
        id=id
    )

    if request.method == "POST":

        form = FeeForm(
            request.POST,
            instance=fee
        )

        if form.is_valid():

            form.save()

            return redirect("fee_list")

    else:

        form = FeeForm(
            instance=fee
        )

    return render(
        request,
        "fees/fee_update.html",
        {
            "form": form
        }
    )


@login_required
def delete_fee(request, id):

    # Principal + HOD
    if not (is_principal(request) or is_hod(request)):
        return redirect("fee_list")

    fee = get_object_or_404(
        Fee,
        id=id
    )

    fee.delete()

    return redirect("fee_list")