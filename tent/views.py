from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tent.models import TentCheck
# Create your views here.


def tent_create_check(request, pk):
    users = User.objects.get(id=pk)
    if request.method == "POST":
        rod = request.POST.get("rod")
        mattress = request.POST.get("mattress")
        zip = request.POST.get("zip")
        rain_cover = request.POST.get("rain_cover")
        ladder = request.POST.get("ladder")
        straps = request.POST.get("straps")

        tent = TentCheck(rod=rod, mattress=mattress, zip=zip,
                         rain_cover=rain_cover, ladder=ladder, straps=straps,
                         user=users)
        tent.save()
        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "tent/tent_create_check.html")


def tent_update_check(request, pk):
    tent = TentCheck.objects.get(pk=pk)
    if request.method == "POST":
        users = User.objects.get(pk=tent.user.pk)
        rod = request.POST.get("rod")
        mattress = request.POST.get("mattress")
        zip = request.POST.get("zip")
        rain_cover = request.POST.get("rain_cover")
        ladder = request.POST.get("ladder")
        straps = request.POST.get("straps")
        active = request.POST.get("active")

        TentCheck.objects.filter(pk=pk).update(rod=rod, mattress=mattress, zip=zip,
                                               rain_cover=rain_cover, ladder=ladder, straps=straps,
                                               user=users, active=active)

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "tent/tent_update_check.html", {"tent": tent})
