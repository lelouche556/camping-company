from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vehicle.models import VehicleCheck
from vehicle.models import Definition, Book
from django.contrib import messages
import datetime
from datetime import date


# Create your views here.


def vehicles(request):
    list1 = []
    now = date.today()
    d0 = request.GET.get("tripDay").replace("-", "")
    duration = request.GET.get("Duration")
    if d0 is '':
        messages.warning(request, "Please fill the date")
        return redirect("app:home")
    if duration is '':
        messages.warning(request, "Please fill the Duration")
        return redirect("app:home")
    check_in = datetime.datetime.strptime(d0, "%Y%m%d").date()
    check_out = check_in + datetime.timedelta(int(duration))

    if check_in < now:
        messages.warning(request, "cant book the car for past date")
        return redirect("app:home")

    definition = Definition.objects.filter(car_type="xenon")
    for _ in definition:
        book = Book.objects.filter(definition=_)
        if book.count() == 0:
            xenon = _
            break
        for b in book:
            if check_in < b.check_in_date and check_out < b.check_in_date or check_in > b.check_out_date \
                    and check_out > b.check_out_date:
                list1.append(1)
            else:
                list1.append(0)
        if 0 in list1:
            xenon = {}
        else:
            xenon = _
            break
        list1 = []

    definition = Definition.objects.filter(car_type="thar")
    for _ in definition:
        book = Book.objects.filter(definition=_)
        if book.count() == 0:
            thar = _
            break
        for b in book:
            if check_in < b.check_in_date and check_out < b.check_in_date or check_in > b.check_out_date \
                    and check_out > b.check_out_date:
                thar = _

            else:
                thar = {}
                break
    return render(request, "vehicle/vehicles.html", {"thar": thar, "xenon": xenon})


def vehicle_info(request):
    return render(request, "vehicle/vehicle_info.html")


def vehicle_create_check(request, pk):
    users = User.objects.get(id=pk)
    if request.method == "POST":
        engine_oil_level = request.POST.get("engine_oil")
        brake_fluid_level = request.POST.get("brake_fluid")
        water_level = request.POST.get("water_level")
        windscreen_washer = request.POST.get("windscreen")
        seatbelts_check = request.POST.get("seatbelts")
        parking_brake = request.POST.get("parking")
        clutch_gearshift = request.POST.get("clutch")
        burning_smell = request.POST.get("burning")
        steering_alignment = request.POST.get("steering")
        dashboard = request.POST.get("dashboard")
        check_lights = request.POST.get("check_lights")
        horn = request.POST.get("horn")
        tyres = request.POST.get("tyres")
        leakage = request.POST.get("leakage")

        vehicle = VehicleCheck(user=users, engine_oil_level=engine_oil_level,
                               brake_fluid_level=brake_fluid_level, water_level=water_level,
                               windscreen_washer=windscreen_washer, seatbelts_check=seatbelts_check,
                               parking_brake=parking_brake, clutch_gearshift=clutch_gearshift,
                               burning_smell=burning_smell, steering_alignment=steering_alignment,
                               dashboard=dashboard, check_lights=check_lights, horn=horn, tyres=tyres,
                               leakage=leakage)
        vehicle.save()
        return redirect("app:show_status", pk=users.pk)
    else:
        return render(request, "vehicle/vehicle_create_check.html")


def vehicle_update_check(request, pk):
    vehicle = VehicleCheck.objects.get(pk=pk, active=True)
    if request.method == "POST":
        users = User.objects.get(pk=vehicle.user.pk)
        engine_oil_level = request.POST.get("engine_oil")
        brake_fluid_level = request.POST.get("water_level")
        water_level = request.POST.get("brake_fluid")
        windscreen_washer = request.POST.get("windscreen")
        seatbelts_check = request.POST.get("seatbelts")
        parking_brake = request.POST.get("parking")
        clutch_gearshift = request.POST.get("clutch")
        burning_smell = request.POST.get("burning")
        steering_alignment = request.POST.get("steering")
        dashboard = request.POST.get("dashboard")
        check_lights = request.POST.get("check_lights")
        horn = request.POST.get("horn")
        tyres = request.POST.get("tyres")
        leakage = request.POST.get("leakage")

        VehicleCheck.objects.filter(pk=pk).update(user=users, engine_oil_level=engine_oil_level,
                                                  brake_fluid_level=brake_fluid_level, water_level=water_level,
                                                  windscreen_washer=windscreen_washer, seatbelts_check=seatbelts_check,
                                                  parking_brake=parking_brake, clutch_gearshift=clutch_gearshift,
                                                  burning_smell=burning_smell, steering_alignment=steering_alignment,
                                                  dashboard=dashboard, check_lights=check_lights, horn=horn, tyres=tyres,
                                                  leakage=leakage)

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "vehicle/vehicle_update_check.html", {"vehicle": vehicle})
