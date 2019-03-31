from django.shortcuts import render, HttpResponse
from payment.models import BillingProfile, Card
from django.http import JsonResponse
import stripe

# Create your views here.

stripe.api_key = "sk_test_t8IRzVYaOAkgHniaZHzr4Bb9"
STRIPE_PUB_KEY = "pk_test_nJn74rHFJDwtw4Tb62fq5sqI"


def add_card(request):
    if request.method == "POST" and request.is_ajax():
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status_code=401)
        token = request.POST.get("token")
        if token is not None:
            customer = stripe.Customer.retrieve(billing_profile.customer_id)
            customer.sources.create(source=token)
            Card.objects.add_new(billing_profile, token)
            return JsonResponse({"message": "Success! Your card was added."})
    return render(request, "payment/add_card.html", {"publish_key": STRIPE_PUB_KEY})
