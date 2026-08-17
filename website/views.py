from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage


# ==========================================================
# HOME
# ==========================================================

def home(request):
    return render(request, "website/home.html")


# ==========================================================
# ABOUT
# ==========================================================

def about(request):
    return render(request, "website/about.html")


# ==========================================================
# HELP
# ==========================================================

def help_page(request):
    return render(request, "website/help.html")


# ==========================================================
# CONTACT
# ==========================================================

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return redirect("contact")

    return render(request, "website/contact.html")