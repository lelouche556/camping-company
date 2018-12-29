from django.shortcuts import render, redirect
from referral.models import Referral
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


@login_required
def referred_view(request, slug):
    if not request.session.get("user_pk"):
        messages.error(request, "Please Log in Again")
        return redirect("app:home")

    default = True
    pk = request.session.get("user_pk")
    user = User.objects.get(pk=pk)
    user1 = Referral.objects.get(user=user)  # one use ref link
    try:
        user2 = Referral.objects.get(slug=slug)  # one ref link used
    except:
        return render(request, "referral/referred.html", {"default": default})
    if user1.referred:
        messages.error(request, "You already referred")
        return redirect("app:home")

    else:
        user2.referred_users.add(user1.user)
        user1.referred_by = user2.user
        user1.referred = True
        user2.save()
        user1.save()
        #request.session["user_pk"] = None  # idk may have security concern
        return render(request, "referral/referred.html", {"user2": user2})