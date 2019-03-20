from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from equipment.models import EquipmentCheck, Inventory

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

        EquipmentCheck.objects.filter(pk=pk).update(user=users, yellow_box=yellow_box,
                                                    kettel=kettel, utensils=utensils, stove=stove,
                                                    bbq_grill=bbq_grill, spare_tyre=spare_tyre,
                                                    shovel=shovel, mug_bucket=mug_bucket
                                                    )

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "equipment/equipment_update_check.html", {"equipment": equipment})


def inventory_create(request, pk):
    users = User.objects.get(id=pk)
    if request.method == "POST":
        degree_8_sleeping = request.POST.get("degree_8_sleeping")
        degree_summer_sleeping = request.POST.get("degree_summer_sleeping")
        kettle = request.POST.get("kettle")
        stove = request.POST.get("stove")
        plates = request.POST.get("plates")
        ground_tent = request.POST.get("ground_tent")
        charger = request.POST.get("charger")
        chairs = request.POST.get("chairs")
        foldable_table_and_chair = request.POST.get("foldable_table_and_chair")
        canister = request.POST.get("canister")

        inventory = Inventory(user=users, degree_8_sleeping=degree_8_sleeping,
                              degree_summer_sleeping=degree_summer_sleeping,
                              kettle=kettle, stove=stove, plates=plates,
                              ground_tent=ground_tent, charger=charger, chairs=chairs,
                              foldable_table_and_chair=foldable_table_and_chair, canister=canister)
        inventory.save()

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "equipment/inventory_create.html")


def inventory_update(request, pk):
    inventory = Inventory.objects.get(pk=pk)
    if request.method == "POST":
        users = User.objects.get(pk=inventory.user.pk)
        degree_8_sleeping = request.POST.get("degree_8_sleeping")
        degree_summer_sleeping = request.POST.get("degree_summer_sleeping")
        kettle = request.POST.get("kettle")
        stove = request.POST.get("stove")
        plates = request.POST.get("plates")
        ground_tent = request.POST.get("ground_tent")
        charger = request.POST.get("charger")
        chairs = request.POST.get("chairs")
        foldable_table_and_chair = request.POST.get("foldable_table_and_chair")
        canister = request.POST.get("canister")

        Inventory.objects.filter(id=pk).update(user=users, degree_8_sleeping=degree_8_sleeping,
                                               degree_summer_sleeping=degree_summer_sleeping,
                                               kettle=kettle, stove=stove, plates=plates,
                                               ground_tent=ground_tent, charger=charger, chairs=chairs,
                                               foldable_table_and_chair=foldable_table_and_chair, canister=canister,
                                               )

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "equipment/inventory_update.html", {"inventory": inventory})

