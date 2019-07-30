from django.shortcuts import render
from destination.models import (Destination, Map,
                                Region, Image,
                                Amenity, Activity,
                                Detail)
from django.http import JsonResponse

# Create your views here.


def destination(request):
    list1 = []
    places = Map.objects.all()
    for x in places:
        print(x.destination.slug)
    if request.is_ajax():
        place = request.POST.get("place")
        region = Region.objects.filter(name__icontains=place)

        for x in region:
            for y in x.region.all():
                list1.append(y.pk)
        data = {"list1": list1}
        return JsonResponse(data)

    return render(request, "destination/destination.html", {"places": places, "list1": list1})


def destination_detail_page(request, slug):
    # Search.objects.new_or_get(request)
    destination = Destination.objects.get(slug=slug)
    image = Image.objects.get(destination=destination)
    activity = Activity.objects.get(destination=destination)
    detail = Detail.objects.get(destination=destination)
    amenity = Amenity.objects.get(destination=destination)
    context = {
               "image": image,
               "destination": destination,
               "amenity": amenity,
               "activity": activity,
               "detail": detail
               }
    return render(request, "destination/detail.html", context)

