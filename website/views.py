from django.shortcuts import render


def home(request):
    return render(request, "website/home.html")


def about(request):
    return render(request, "website/about.html")


def help_page(request):
    return render(request, "website/help.html")


def contact(request):
    return render(request, "website/contact.html")