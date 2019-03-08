from django.shortcuts import render
from destination.models import Destination

# Create your views here.


def destination(request):
    items = Destination.objects.all()
    return render(request, "destination/destination.html", {"items": items})


def destination_detail_page(request, slug):
    # Search.objects.new_or_get(request)
    item = Destination.objects.get(slug=slug)
    context = {"item": item}
    return render(request, "destination/detail.html", context)

