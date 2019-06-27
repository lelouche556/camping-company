import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import render, redirect
from django.http import JsonResponse
from paywix.payu import PAYU
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from pay.models import Pay


# Create your views here.

# Import Payu from PAYWIX

payu = PAYU()


@login_required
def checkout(request):
    user = User.objects.get(pk=request.user.pk)
    payment = Pay.objects.get(user=user)
    hash_object = hashlib.sha256(b'randint(0,20)')
    txnid = hash_object.hexdigest()[0:20]
    payment_data = {
        'txnid': txnid,
        'amount': str(payment.amount),
        'firstname': payment.firstname,
        'email': payment.email,
        'phone': payment.phone,
        'productinfo': 'car book'
    }
    payment.txnid = txnid
    payment.productinfo = 'car book'
    payment.save()
    payu_data = payu.initate_transaction(payment_data)
    if request.is_ajax():
        request.POST.get("total")
        return JsonResponse(payu_data)
    return render(request, "payment/checkout.html", {"posted": payu_data})


# Success URL
@csrf_protect
@csrf_exempt
def payment_success(request):
    # Payu will return response success data with hash value
    # Need to verify the data with payu check_hash
    print(request.user.is_authenticated)
    try:
        payu_success_data = payu.check_hash(dict(request.POST))
        status = payu_success_data["data"]["status"]
        txn = payu_success_data["data"]["txnid"]
        amount = payu_success_data["data"]["amount"]
        success = {
            "status": status,
            "txnid": txn,
            "amount": amount
        }
        return render(request, "payment/success.html", success)
    except:
        return redirect("app:home")


# Failure URL
@csrf_protect
@csrf_exempt
def payment_failure(request):

    payu_failure_data = payu.check_hash(dict(request.POST))

    return render(request, "payment/failure.html")


@login_required
def cart(request):
    user = User.objects.get(pk=request.user.pk)
    payment = Payment.objects.get(user=user)
    # if not request.POST.get("status"):
    #     return redirect("app:home")
    if request.is_ajax():
        amount = round(float(request.POST.get("total")))
        payment.amount = amount
        payment.save()
        return JsonResponse({"success": "success"})
    return render(request, "payment/cart.html")