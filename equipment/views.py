from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from equipment.models import EquipmentCheck

# Create your views here.


def equipment_create_check(request, pk):
    users = User.objects.get(id=pk)
    if request.method == "POST":
        yellow_box = request.POST.get("yellow_box")
        kettel = request.POST.get("kettel")
        utensils = request.POST.get("utensils")
        stove = request.POST.get("stove")
        bbq_grill = request.POST.get("bbq_grill")
        spare_tyre = request.POST.get("spare_tyre")
        shovel = request.POST.get("shovel")
        mug_bucket = request.POST.get("mug_bucket")

        equipment = EquipmentCheck(user=users, yellow_box=yellow_box,
                                   kettel=kettel, utensils=utensils, stove=stove,
                                   bbq_grill=bbq_grill, spare_tyre=spare_tyre,
                                   shovel=shovel, mug_bucket=mug_bucket
                                             )
        equipment.save()
        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "equipment/equipment_create_check.html")


def equipment_update_check(request, pk):
    equipment = EquipmentCheck.objects.get(pk=pk)
    if request.method == "POST":
        users = User.objects.get(pk=equipment.user.pk)
        yellow_box = request.POST.get("yellow_box")
        kettel = request.POST.get("kettel")
        utensils = request.POST.get("utensils")
        stove = request.POST.get("stove")
        bbq_grill = request.POST.get("bbq_grill")
        spare_tyre = request.POST.get("spare_tyre")
        shovel = request.POST.get("shovel")
        mug_bucket = request.POST.get("mug_bucket")
        active = request.POST.get("active")

        EquipmentCheck.objects.filter(pk=pk).update(user=users, yellow_box=yellow_box,
                                                    kettel=kettel, utensils=utensils, stove=stove,
                                                    bbq_grill=bbq_grill, spare_tyre=spare_tyre,
                                                    shovel=shovel, mug_bucket=mug_bucket, active=active
                                                    )

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "equipment/equipment_update_check.html", {"equipment": equipment})