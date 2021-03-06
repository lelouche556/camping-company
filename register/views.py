from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib import messages
from referral.models import Referral
from app.utils import *
from pay.models import Pay
import re
from django.utils.http import is_safe_url
from django.http import JsonResponse
from register.models import Password
from datetime import date

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_n = User.objects.filter(username=username)
        user_e = User.objects.filter(email=email)
        password1 = request.POST.get("password1")
        code = request.POST.get("slug")

        if user_n.count() == 1 or user_e.count() == 1:
            messages.warning(request, "Username/email already taken or log in to complete signup")
            return redirect("register:signin")

        if code is "":

            '''If referral code is empty'''
            user = User.objects.create_user(username=username, email=email)
            Referral(user=user).save()
            user.set_password(password1)
            user.save()
            login(request, user)
            Pay(user=user, email=email).save()
            #Customer(user=user).save()
            return redirect("register:welcome")
        try:
            ref_user = Referral.objects.get(slug=code)
        except:
            messages.warning(request, "Wrong referral code")
            return redirect("register:signin")

        '''If referral code is not empty'''
        user = User.objects.create_user(username=username, email=email)
        referral = Referral(user=user, referred_by=ref_user.user, referred=True)
        ref_user.referred_users.add(user)
        user.set_password(password1)
        user.save()
        referral.save()
        ref_user.save()
        login(request, user)
        Pay(user=user, email=email).save()
        #Customer(user=user).save()
        message_to_customer(email)

        return redirect("register:welcome")

    else:
        return render(request, "register/signin.html")


def signin(request):
    next_ = request.GET.get('next')
    if request.method == "POST":
        next_post = request.POST.get('next')
        next_post = next_post.replace("k", "/")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if re.search("@", username):
            try:
                u = User.objects.get(email=username)
                user = authenticate(username=u.username, password=password)
            except:
                messages.warning(request, "You Need to sign up first")
                return redirect("app:home")
        else:
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
                    request.session["user_pk"] = user.pk
                else:
                    login(request, user)
                    messages.warning(request, "Complete sign up")
                    return redirect("register:welcome")

                if next_post != "None":  # not used is_safe_url  here next post is none (a string)
                    return redirect(next_post)
                else:
                    return redirect("customer:user_page")
        else:
            messages.warning(request, "Password/Username is wrong")
            return redirect("register:signin")
    return render(request, "register/signin.html", {"next": next_})


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
        customer = Customer(user=user, phone=number, city=city,
                            address=address, nickname=nickname,
                            license_number=license_number, about=about,
                            terms_condition=True)
        customer.save()
        message_to_company(email=user.email, message="someone signed up yay!! :)",
                           name=fname, phone=number,
                           subject="Leads Team Rock and Roll")

        Pay.objects.filter(user=user).update(firstname=fname, phone=number)

        return redirect("customer:user_page")
    return render(request, "register/welcome.html")


def pass_reset(request):

    if request.is_ajax():
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({"error":"User does not exist"})
        password = Password(email=email)
        password.save()
        print()
        password_reset(name=user.first_name,email=email,subject="Password reset",link=password.reset_link)
        return JsonResponse({"success":"success"})

    slug = request.session.get("slug")

    if request.method == "POST":
        pass_resettor = Password.objects.get(slug=slug)
        user = User.objects.get(email=pass_resettor.email)
        password = request.POST.get("password1")
        user.set_password(password)
        user.save()
        pass_resettor.active = False
        pass_resettor.save()
        messages.success(request,"Password change successfully")
        return redirect("app:home")

    try:
        pass_resettor = Password.objects.get(slug=slug)
        if not pass_resettor.active and pass_resettor.used:
            del request.session["slug"]
    except:
        return render(request, "register/pass_reset.html",{"pass_resettor":{"used":False}})
    return render(request, "register/pass_reset.html",{"pass_resettor":pass_resettor})


def pass_rediretor(request,slug):
    now = date.today()
    pass_resettor = Password.objects.get(slug=slug)
    request.session["slug"] = slug
    if pass_resettor.initiate_date == now:
        pass_resettor.used = True
        pass_resettor.save()
        return redirect("register:pass_reset")
    else:
        pass_resettor.active = False
        pass_resettor.save()
    return redirect("register:pass_reset")
