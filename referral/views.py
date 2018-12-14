from django.shortcuts import render
from referral.models import Referral
from django.contrib.sessions.models import Session

# Create your views here.


def referred_view(request, slug):
    k = Session.objects.get(pk=Session.pk)
    print(k)
    default = True
    check = Referral.objects.get(slug=slug)
    if check is None:
        default = False
    #check.referred = True
    return render(request, "referral/referred.html", {"check": check, "default": default})

# in login get session data of pk of user