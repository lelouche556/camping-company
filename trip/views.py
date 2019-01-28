from django.shortcuts import render, redirect
from trip.models import Trip
from django.contrib.auth.models import User

from django.utils.dateparse import parse_date, parse_time

# Create your views here.


def trip_create(request, pk):

    if request.method == "POST":
        user = User.objects.get(id=pk)
        check_in_date = parse_date(request.POST.get("startdate"))
        check_out_date = parse_date(request.POST.get("enddate"))
        check_in_time = parse_time(request.POST.get("starttime"))
        check_out_time = parse_time(request.POST.get("endtime"))
        duration_of_trip = request.POST.get("duration")
        amount_paid = request.POST.get("amount")
        destination = request.POST.get("destination")
        residence_address = request.POST.get("addr")
        trip_status = request.POST.get("tripstatus")
        car_type = request.POST.get("cartype")
        guest = request.POST.get("guests")

        Trip.objects.get_or_create(check_in_date=check_in_date, check_out_date=check_out_date,
                                   check_in_time=check_in_time, check_out_time=check_out_time,
                                   duration_of_trip=duration_of_trip, amount_paid=amount_paid,
                                   destination=destination, residence_address=residence_address,
                                   trip_status=trip_status, car_type=car_type, user=user, guest=guest)
        return redirect("app:create_status", pk=user.pk)

    else:
        return render(request, "trip/trip_create.html")


def trip_update(request, pk):
    trip = Trip.objects.get(pk=pk, active=True)
    if request.method == "POST":
        users = User.objects.get(id=trip.user.pk)
        check_in_date = parse_date(request.POST.get("startdate"))
        check_out_date = parse_date(request.POST.get("enddate"))
        check_in_time = parse_time(request.POST.get("starttime"))
        check_out_time = parse_time(request.POST.get("endtime"))
        duration_of_trip = request.POST.get("duration")
        amount_paid = request.POST.get("amount")
        destination = request.POST.get("destination")
        residence_address = request.POST.get("addr")
        trip_status = request.POST.get("tripstatus")
        car_type = request.POST.get("cartype")

        Trip.objects.update(check_in_date=check_in_date, check_out_date=check_out_date,
                            check_in_time=check_in_time, check_out_time=check_out_time,
                            duration_of_trip=duration_of_trip, amount_paid=amount_paid,
                            destination=destination, residence_address=residence_address,
                            trip_status=trip_status, car_type=car_type, user=users)
        trip = Trip.objects.get(pk=pk, active=True)
        trip.save()
        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "trip/trip_update.html", {"trip": trip})