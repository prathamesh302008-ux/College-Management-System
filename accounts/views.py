from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):

    # Agar user already login hai
    if request.user.is_authenticated:
        return redirect("/dashboard/")

    if request.method == "POST":

        # Remove extra spaces
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        role = request.POST.get("role", "").strip()

        print("=" * 50)
        print(f"Username = [{username}]")
        print(f"Password = [{password}]")
        print(f"Role = [{role}]")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        print("Authenticate Result :", user)

        if user is not None:

            try:

                profile = user.userprofile

                print("Database Role :", profile.role)

                if profile.role != role:

                    return render(
                        request,
                        "accounts/login.html",
                        {
                            "error": "Selected Role is Incorrect"
                        }
                    )

                login(request, user)

                print("Login Successful")

                return redirect("/dashboard/")

            except Exception as e:

                print("Profile Error :", e)

                return render(
                    request,
                    "accounts/login.html",
                    {
                        "error": "User Profile Not Found"
                    }
                )

        else:

            print("Authentication Failed")

            return render(
                request,
                "accounts/login.html",
                {
                    "error": "Invalid Username or Password"
                }
            )

    return render(
        request,
        "accounts/login.html"
    )


def logout_view(request):

    logout(request)

    return redirect("login")