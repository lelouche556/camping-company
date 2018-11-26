from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user = User.objects.filter(username=username)
        password1 = request.POST.get("password1")
        if user.count() == 1:
            messages.error(request, "Username/email already taken")
            return redirect("register:signin")

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password1)

        user.save()
        login(request, user)
        return redirect("register:welcome")

    else:
        return render(request, "register/signin.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("app:represent")
            else:
                customer = Customer.objects.filter(user=user)
                if customer.count() == 1:
                    login(request, user)
                    messages.success(request, "Logged in")
                else:
                    login(request, user)
                    messages.error(request, "Complete sign up")
                    return redirect("register:welcome")
                return redirect("customer:user_page")
        else:
            messages.error(request, "Password/Username is wrong")
            return redirect("register:signin")
    return render(request, "register/signin.html")


@login_required
def sign_out(request):
    logout(request)
    return redirect("app:home")


@login_required
def welcome(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        license_number = request.POST.get("license_number")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        number = request.POST.get("number")
        city = request.POST.get("city")
        nickname = request.POST.get("nickname")
        about = request.POST.get("about")
        address = request.POST.get("address")
        user.first_name = fname
        user.last_name = lname
        user.number = number
        user.save()
        Customer.objects.get_or_create(phone=number, user=user, city=city,
                                       address=address, nickname=nickname,
                                       license_number=license_number, about=about,
                                       terms_condition=True)

        return redirect("customer:user_page")
    return render(request, "register/welcome.html")
