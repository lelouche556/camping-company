from django.shortcuts import render
from destination.models import (Destination, Map,
                                Region, Image,
                                Amenity, Activity,
                                Detail, Circuit)
from django.http import JsonResponse
import os
# Create your views here.


def destination(request):
    list1 = []
    maps = os.environ.get("maps")
    places = Map.objects.all().order_by("pk")
    if request.is_ajax():
        place = request.POST.get("place")
        region = Region.objects.filter(name__icontains=place)

        for x in region:
            for y in x.region.all():
                list1.append(y.pk)
        data = {"list1": list1}
        return JsonResponse(data)

    return render(request, "destination/destination.html", {"places": places, "maps": maps,"list1":list1})


def destination_detail_page(request, slug):
    # Search.objects.new_or_get(request)
    destination = Destination.objects.get(slug=slug)
    try:
        image = Image.objects.get(destination=destination)
    except:
        return render(request, "destination/detail.html", {"Data":"data available soon"})
    activity = Activity.objects.get(destination=destination)
    detail = Detail.objects.get(destination=destination)
    amenity = Amenity.objects.get(destination=destination)
    place = destination.place
    place = 'kdestinationk' + place
    place = place.replace(" ", "-")
    context = {
               "image": image,
               "destination": destination,
               "amenity": amenity,
               "activity": activity,
               "detail": detail,
               "place": place
               }

    if request.method == "POST":
        print(request.POST.get("some"))

        return JsonResponse({"amount": 100, "email": "kanishk.tanwar7@gmail.com",
                             "name": "kanishk",
                             "razor_id": "rzp_test_jhx8CJoTQCL3Eh"
                             })

    if request.is_ajax():
        return JsonResponse({"amount": 100, "email": "kanishk.tanwar7@gmail.com",
                             "name": "kanishk",
                             "razor_id": "rzp_test_jhx8CJoTQCL3Eh"
                             })
    return render(request, "destination/detail.html", context)


def circuits(request):
    return render(request, "destination/circuits.html")


def circuit(request, slug):
    cir = Circuit.objects.get(slug=slug)
    return render(request, "destination/circuit.html", {"cir": cir})

