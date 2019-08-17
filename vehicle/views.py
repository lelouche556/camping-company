from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vehicle.models import VehicleCheck
from vehicle.models import Definition,Book
from django.contrib import messages
import datetime
from datetime import date


# Create your views here.


def vehicles(request):
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

    book1 = Book.objects.filter(car_name="xenon")
    thar = {}
    xenon = {}
    if book1.count() != 0:
        for _ in book1:
            if now == _.check_out_date:
                _.delete()
            if check_in < _.check_in_date and check_out < _.check_in_date or check_in > _.check_out_date:
                book = Book.objects.filter(check_in_date=check_in, check_out_date=check_out)
                if book.count() == 4:
                    xenon = {}
                    break
                else:
                    xenon = Definition.objects.get(car_name="xenon")
                    break
    else:
        xenon = Definition.objects.get(car_name="xenon")

    book2 = Book.objects.filter(car_name="thar")
    if book2.count() != 0:
        for _ in book2:
            if now == _.check_out_date:
                _.delete()
            if check_in < _.check_in_date and check_out < _.check_in_date or check_in > _.check_out_date:
                book = Book.objects.filter(check_in_date=check_in,check_out_date=check_out)
                if book.count() == 1:
                    thar = {}
                    break
                else:
                    thar = Definition.objects.get(car_name="thar")
                    break
    else:
        thar = Definition.objects.get(car_name="thar")

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
