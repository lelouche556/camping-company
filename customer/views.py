from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from destination.models import Destination
from .models import Customer
from itinerary.models import Itinerary
from django.contrib.auth.models import User
import requests
import os
# Create your views here.


# def destination(request):
#     return render(request, "customer/create_itinerary.html")

def simple_message(name, email, subject, message):
    return requests.post(
        os.environ.get("MAILGUN_URL"),
        auth=("api", os.environ.get("MAILGUN_API_KEY")),
        data={"from": os.environ.get("MAILGUN_FROM"),
              "to": os.environ.get("email"),
              "subject": subject,
              "text": "Name of the person queried : {} \nEmail of the person queried : "
                      "{} \nQuery : {}".format(name, email, message)
              })


@login_required
def user_page(request):
    customer = Customer.objects.get(user=request.user)
    return render(request, "customer/user_page.html", {"customer": customer})


@login_required
def create_itinerary(request):
    # Search.objects.new_or_get(request)
    items = Destination.objects.all()
    try:
        itinerary = Itinerary.objects.get(user=request.user, active=True)
    except:
        return render(request, "customer/create_itinerary.html", {"items": items})
    context = {"items": items, "itinerary": itinerary}
    return render(request, "customer/create_itinerary.html", context)


@login_required
def delete_itinerary(request):
    try:
        itinerary = Itinerary.objects.get(user=request.user, active=True)
    except Itinerary.DoesNotExist:
        raise Http404("No Itinerary found, Create one To delete")
    itinerary.delete()
    return redirect("customer:create_itinerary")


@login_required
def trip_detail(request):
    users = User.objects.get(pk=request.user.pk)
    return render(request, "customer/trip_status.html", {"users":users})


def itinerary_detail_page(request, pk):
    # Search.objects.new_or_get(request)
    item = Destination.objects.get(pk=pk)
    context = {"item": item}
    return render(request, "customer/detail.html", context)


@login_required
def custom_itinerary(request):
    data = Itinerary.objects.filter(user=request.user, active=True)
    list1 = []
    list2 = []
    hour = 12
    for x in data:
        for y in x.destination.all():
            if hour-y.hours >= 0:
                list2.append(y.pk)
                hour = hour - y.hours
            else:
                list1.append(list2)
                list2 = []
                list2.append(y.pk)
                hour = 12
        list1.append(list2)

    if request.is_ajax():
        message = request.POST.get("places")
        list1 = [int(s) for s in message.split(',')]
        itinerary = Itinerary(user=request.user)
        itinerary.save()
        for x in list1:
            destination = Destination.objects.get(pk=x)
            itinerary.destination.add(destination)
    return render(request, "customer/custom.html", {"data": data, "list": list1})


@login_required
def book(request, pk):
    user = User.objects.get(pk=pk)
    email = str(user.email)
    name = str(user.first_name)
    subject = str("Booking")
    message = str("{} just Booked a car :D name {} phone {}".format(name, user.first_name, user.customer_check.phone))
    simple_message(name, email, subject, message)
    return render(request, "customer/success.html")