from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vehicle.models import VehicleCheck
from vehicle.models import Definition
from datetime import date
from django.contrib import messages


# Create your views here.


def vehicles(request):
    arr = []
    list1 = []
    d0 = request.GET.get("tripDay").split("-")
    duration = request.GET.get("Duration")
    if d0[0] is '':
        messages.warning(request, "Please fill the date")
        return redirect("app:home")
    if duration is '':
        messages.warning(request, "Please fill the Duration")
        return redirect("app:home")

    vehicle = Definition.objects.all()
    for x in vehicle:
        if x.check_out_date is None:
            continue
        d1 = x.check_out_date
        days_diff = (date(int(d0[0]), int(d0[1]), int(d0[2])) - date(d1.year, d1.month, d1.day)).days
        if days_diff >= 0:
            arr.append(1)
        else:
            arr.append(0)
        list1 = zip(vehicle, arr)
    return render(request, "vehicle/vehicles.html", {"list1": list1})


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
