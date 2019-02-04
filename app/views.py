import os
from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from trip.models import Trip
from destination.models import Destination
from django.contrib import messages
from django.http import JsonResponse

import requests

# Create your views here.


def simple_message(name, email, subject, message, phone):
    return requests.post(
        os.environ.get("MAILGUN_URL"),
        auth=("api", os.environ.get("MAILGUN_API_KEY")),
        data={"from": os.environ.get("MAILGUN_FROM"),
              "to": os.environ.get("email"),
              "subject": subject,
              "text": "Name of the person queried : {} \n phone number of person {} \nEmail of the person queried : "
                      "{} \nQuery : {}".format(name, phone, email, message)
              })


def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")


def terms_condition(request):
    return render(request, "app/terms_condition.html")


def calender(request):
    if request.user.is_superuser:
        x = Trip.objects.filter(trip_status="ongoing")
        y = Trip.objects.filter(trip_status="ongoing")

        for thar in x:
            thar = thar

        for xenon in y:
            xenon = xenon

        if x.count() == 1 and y.count() == 1:
            context = {
                "thar": thar,
                "Xenon": xenon
            }
        else:
            raise Http404("You Did not have save previous trips as ended please fix and try again")

        return render(request, "app/calender.html", context)

    else:
        return redirect("customer:user_page")


def findus(request):
    if request.method == "POST":
        email = str(request.POST.get("email"))
        name = str(request.POST.get("name"))
        phone = str(request.POST.get("phone"))
        subject = "Query"
        message = str(request.POST.get("message"))
        simple_message(name, email, subject, message, phone)
        messages.success(request, "Your message sent")
        return redirect("app:findus")
    else:
        return render(request, "app/findus.html")


@login_required
def show_status(request, pk):
    if request.user.is_superuser:
        users = User.objects.get(pk=pk)
        trcount = users.trip_check.filter(user=users, active=True).count()
        ecount = users.equipment_check.filter(user=users, active=True).count()
        vcount = users.vehicle_check.filter(user=users, active=True).count()
        tcount = users.tent_check.filter(user=users, active=True).count()
        return render(request, "app/show.html", {"users": users,"ecount": ecount, "tcount": tcount,
                                                 "vcount": vcount, "trcount": trcount})
    else:
        return redirect("customer:user_page")


@login_required
def represent(request):
    if request.user.is_superuser:
        if request.is_ajax():
            email = request.POST.get("email")
            try:
                user = User.objects.get(email=email)
                pk = user.pk
                data = {
                    "id": pk
                }
                return JsonResponse(data)
            except:
                data = {
                    "id": 0
                }
                return JsonResponse(data)

        trips = Trip.objects.all()
        users = User.objects.all()
        return render(request, "app/represent.html", {"trips": trips, "users": users})
    else:
        return redirect("customer:user_page")


def destination(request):
    items = Destination.objects.all()
    return render(request, "app/destination.html", {"items": items})


def faq(request):
    return render(request, "app/faq.html")


def sitemap(request):
    return render(request, "app/sitemap.xml")