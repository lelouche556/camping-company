from django.shortcuts import render, HttpResponse, redirect
from payment.models import BillingProfile, Card, Charge
from django.http import JsonResponse
import stripe

# Create your views here.

stripe.api_key = "sk_test_t8IRzVYaOAkgHniaZHzr4Bb9"
STRIPE_PUB_KEY = "pk_test_nJn74rHFJDwtw4Tb62fq5sqI"


def checkout(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            Card.objects.add_new(billing_profile, token)
            Charge.objects.do(billing_profile=billing_profile, total=round(float(request.POST.get("total")),2))
            return JsonResponse({"message": "Success! Your card was added."})
        else:
            return redirect("/")
    return render(request, "payment/checkout.html", {"publish_key": STRIPE_PUB_KEY})


def cart(request):
    return render(request, "payment/cart.html")
