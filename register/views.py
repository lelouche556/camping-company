from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from customer.models import Customer
from django.contrib import messages
from referral.models import Referral
import requests
import os
# Create your views here.


def return_message(email):
    return requests.post(
        os.environ.get("MAILGUN_URL"),
        auth=("api", os.environ.get("MAILGUN_API_KEY")),
        data={"from": os.environ.get("MAILGUN_FROM"),
              "to": [email],
              "subject": "Hello",
              "html": '<html><head><meta content="text/html; charset=UTF-8" http-equiv="content-type"><style type="text/css">ul.lst-kix_jbfewle4fqj4-6{list-style-type:none}.lst-kix_jbfewle4fqj4-0>li:before{content:"\0025cf  "}ul.lst-kix_jbfewle4fqj4-5{list-style-type:none}ul.lst-kix_jbfewle4fqj4-8{list-style-type:none}ul.lst-kix_jbfewle4fqj4-7{list-style-type:none}ul.lst-kix_jbfewle4fqj4-2{list-style-type:none}.lst-kix_jbfewle4fqj4-1>li:before{content:"\0025cb  "}ul.lst-kix_jbfewle4fqj4-1{list-style-type:none}.lst-kix_jbfewle4fqj4-2>li:before{content:"\0025a0  "}ul.lst-kix_jbfewle4fqj4-4{list-style-type:none}ul.lst-kix_jbfewle4fqj4-3{list-style-type:none}.lst-kix_jbfewle4fqj4-3>li:before{content:"\0025cf  "}.lst-kix_jbfewle4fqj4-4>li:before{content:"\0025cb  "}.lst-kix_jbfewle4fqj4-7>li:before{content:"\0025cb  "}.lst-kix_jbfewle4fqj4-8>li:before{content:"\0025a0  "}.lst-kix_jbfewle4fqj4-5>li:before{content:"\0025a0  "}.lst-kix_jbfewle4fqj4-6>li:before{content:"\0025cf  "}ul.lst-kix_jbfewle4fqj4-0{list-style-type:none}ol{margin:0;padding:0}table td,table th{padding:0}.c26{border-right-style:solid;padding:5pt 5pt 5pt 5pt;border-bottom-color:#ffffff;border-top-width:1pt;border-right-width:1pt;border-left-color:#ffffff;vertical-align:top;border-right-color:#ffffff;border-left-width:1pt;border-top-style:solid;border-left-style:solid;border-bottom-width:1pt;width:648pt;border-top-color:#ffffff;border-bottom-style:solid}.c13{color:#38761d;font-weight:700;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Verdana";font-style:normal}.c0{color:#38761d;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Verdana";font-style:normal}.c2{color:#434343;font-weight:400;text-decoration:none;vertical-align:baseline;font-size:11pt;font-family:"Verdana";font-style:italic}.c9{padding-top:12pt;padding-bottom:0pt;line-height:1.38;orphans:2;widows:2;text-align:left}.c21{padding-top:12pt;padding-bottom:0pt;line-height:1.5;orphans:2;widows:2;text-align:left}.c25{padding-top:0pt;padding-bottom:0pt;line-height:1.15;orphans:2;widows:2;text-align:left}.c4{padding-top:6pt;padding-bottom:0pt;line-height:1.5;orphans:2;widows:2;text-align:left}.c5{padding-top:12pt;padding-bottom:0pt;line-height:1.0;orphans:2;widows:2;text-align:left}.c10{-webkit-text-decoration-skip:none;color:#434343;text-decoration:underline;text-decoration-skip-ink:none;font-style:italic}.c11{color:#000000;text-decoration:none;vertical-align:baseline;font-size:11pt;font-style:normal}.c3{border-spacing:0;border-collapse:collapse;margin-right:auto}.c23{text-decoration:none;vertical-align:baseline;font-size:11pt;font-style:italic}.c19{text-decoration:none;vertical-align:baseline;font-size:11pt;font-style:normal}.c15{-webkit-text-decoration-skip:none;color:#1155cc;text-decoration:underline;text-decoration-skip-ink:none}.c28{vertical-align:baseline;font-size:11pt;font-style:normal}.c6{background-color:#d9ead3;max-width:648pt;padding:72pt 72pt 72pt 72pt}.c22{margin-left:72pt;padding-left:0pt}.c18{font-style:italic;color:#434343}.c12{color:inherit;text-decoration:inherit}.c20{font-family:"Verdana";font-weight:700}.c14{font-weight:400;font-family:"Arial"}.c7{font-weight:400;font-family:"Verdana"}.c1{padding:0;margin:0}.c16{color:#38761d}.c24{font-size:12pt}.c8{color:#222222}.c17{height:11pt}.c27{height:87pt}.title{padding-top:0pt;color:#000000;font-size:26pt;padding-bottom:3pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}.subtitle{padding-top:0pt;color:#666666;font-size:15pt;padding-bottom:16pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}li{color:#000000;font-size:11pt;font-family:"Arial"}p{margin:0;color:#000000;font-size:11pt;font-family:"Arial"}h1{padding-top:20pt;color:#000000;font-size:20pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h2{padding-top:18pt;color:#000000;font-size:16pt;padding-bottom:6pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h3{padding-top:16pt;color:#434343;font-size:14pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h4{padding-top:14pt;color:#666666;font-size:12pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h5{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;orphans:2;widows:2;text-align:left}h6{padding-top:12pt;color:#666666;font-size:11pt;padding-bottom:4pt;font-family:"Arial";line-height:1.15;page-break-after:avoid;font-style:italic;orphans:2;widows:2;text-align:left}</style></head><body class="c6"><p class="c25"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 864.00px; height: 114.67px;"><img alt="" src="https://s3.ap-south-1.amazonaws.com/camping-company/media/emails/image3.png" style="width: 864.00px; height: 114.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span></p><p class="c25"><span class="c19 c7 c8">Hello Friend,</span></p><p class="c4"><span class="c19 c7 c8">Thanks for reaching out. We&#39;d be happy to answer all your questions.</span></p><p class="c21"><span class="c13">Who are we?</span></p><p class="c9"><span class="c7">Nature has a subtle way of enhancing consciousness, mindfulness, and awareness. With this belief, The Camping Company was created to provide a platform to have an immersive experience with nature. It enables travelers to explore the unexplored with the help of SUVs, jeeps equipped with rooftop tents and camping gears for a comfortable overlanding expedition. It&#39;s a self-drive rental model.</span></p><p class="c9"><span class="c7 c8">You can check out our youtube channel for a glimpse of overlanding trips - </span><span class="c15 c7"><a class="c12" href="https://www.google.com/url?q=https://www.youtube.com/watch?v%3DIRMbGsYYB-A&amp;sa=D&amp;ust=1550562095223000">From the inside</a></span><span class="c7 c8">; </span><span class="c7 c15"><a class="c12" href="https://www.google.com/url?q=https://www.youtube.com/watch?v%3DzwZ1vMuSvTo%26t%3D19s&amp;sa=D&amp;ust=1550562095223000">Road trips in Meghalaya | Nongkhnum Island</a></span><span class="c7 c8">; </span><span class="c15 c7"><a class="c12" href="https://www.google.com/url?q=https://www.youtube.com/watch?v%3DRYJaLK4POaU&amp;sa=D&amp;ust=1550562095224000">Top 10 destinations in Meghalaya</a></span><span class="c7 c8">, </span><span class="c15 c7"><a class="c12" href="https://www.google.com/url?q=https://www.youtube.com/watch?v%3DF4Phzzct7J0&amp;sa=D&amp;ust=1550562095224000">What is Overlanding</a></span><span class="c7 c8">, </span><span class="c7 c8 c24">&nbsp;</span><span class="c15 c7"><a class="c12" href="https://www.google.com/url?q=https://www.youtube.com/watch?v%3DdGBBiEqM5Zg&amp;sa=D&amp;ust=1550562095224000">Overlanding in Arunachal - E01</a></span><span class="c7 c8">; </span><span class="c15 c7"><a class="c12" href="https://www.google.com/url?q=https://www.youtube.com/watch?v%3DdGBBiEqM5Zg&amp;sa=D&amp;ust=1550562095225000">Overlanding in Arunachal - E02</a></span></p><ul class="c1 lst-kix_jbfewle4fqj4-0 start"><li class="c9 c22"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 652.50px; height: 461.59px;"><a href="https://www.youtube.com/channel/UC6mvUrWd2m4KbokMSALM0Hw"><img alt="" src="https://s3.ap-south-1.amazonaws.com/camping-company/media/emails/image2.png" style="width: 652.50px; height: 461.59px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></a></span></li></ul><p class="c9"><span class="c7 c16">Expedition Itinerary: </span><span class="c7">We curate a circuit for the overlanding expedition which enables the adventurer/s to explore the state and live the dream of sleeping under the stars every night at a different location. It&rsquo;s customized according to the adventurer&rsquo;s needs and comforts. </span><span class="c0">&nbsp;</span></p><p class="c9"><span class="c16 c20">How it works?</span></p><p class="c9"><span style="overflow: hidden; display: inline-block; margin: 0.00px 0.00px; border: 0.00px solid #000000; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px); width: 864.00px; height: 230.67px;"><img alt="" src="https://s3.ap-south-1.amazonaws.com/camping-company/media/emails/image1.png" style="width: 864.00px; height: 230.67px; margin-left: 0.00px; margin-top: 0.00px; transform: rotate(0.00rad) translateZ(0px); -webkit-transform: rotate(0.00rad) translateZ(0px);" title=""></span><span class="c0">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span></p><a id="t.f142ae7cd93afed253db01f9cf0761382029a555"></a><a id="t.0"></a><table class="c3"><tbody><tr class="c27"><td class="c26" colspan="1" rowspan="1"><p class="c5"><span class="c7 c16">Tariff</span><span class="c7 c11">: Rs.3000/night for 2 adventurers and Rs.350 each after 2.</span></p><p class="c5"><span class="c7">It includes: Car, Rooftop tent (which sleeps, 3 medium sized individuals), Expedition Itinerary, Sleeping bags, Camping equipment ( Rs.1500 for the expedition)</span></p></td></tr></tbody></table><p class="c9"><span class="c2">Please reach out to us on below-mentioned details for any questions.</span></p><p class="c5"><span class="c2">Team</span></p><p class="c5"><a href="https://www.camping-co.com"><span class="c2">The Camping Co - www.camping-co.com</span></a></p><p class="c5"><span class="c7 c18">Email - </span><span class="c7 c10"><a class="c12" href="mailto:info@camping-co.com">info@camping-co.com</a></span></p><p class="c5 c17"><span class="c0"></span></p><p class="c5 c17"><span class="c7 c8 c23"></span></p><p class="c17 c25"><span class="c11 c14"></span></p></body></html>'
              })


def signup(request):

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        user_n = User.objects.filter(username=username)
        user_e = User.objects.filter(email=email)
        password1 = request.POST.get("password1")
        code = request.POST.get("slug")

        if user_n.count() == 1 or user_e.count() == 1:
            messages.warning(request, "Username/email already taken or log in to complete signup")
            return redirect("register:signin")

        if code is "":
            user = User.objects.create_user(username=username, email=email)
            Referral(user=user).save()
            user.set_password(password1)
            user.save()
            login(request, user)
            return redirect("register:welcome")
        try:
            ref_user = Referral.objects.get(slug=code)
        except:
            messages.warning(request, "Wrong referral code")
            return redirect("register:signin")
        user = User.objects.create_user(username=username, email=email)
        referral = Referral(user=user, referred_by=ref_user.user, referred=True)
        ref_user.referred_users.add(user)
        user.set_password(password1)
        user.save()
        referral.save()
        ref_user.save()
        login(request, user)
        return_message(email)

        return redirect("register:welcome")

    else:
        return render(request, "register/signin.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("app:represent")
            else:
                customer = Customer.objects.filter(user=user)
                if customer.count() == 1:
                    login(request, user)
                    messages.success(request, "Logged in")
                    request.session["user_pk"] = user.pk
                else:
                    login(request, user)
                    messages.warning(request, "Complete sign up")
                    return redirect("register:welcome")
                return redirect("customer:user_page")
        else:
            messages.warning(request, "Password/Username is wrong")
            return redirect("register:signin")
    return render(request, "register/signin.html")


@login_required
def sign_out(request):
    logout(request)
    return redirect("app:home")


@login_required
def welcome(request):
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        license_number = request.POST.get("license_number")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        number = request.POST.get("number")
        city = request.POST.get("city")
        nickname = request.POST.get("nickname")
        about = request.POST.get("about")
        address = request.POST.get("address")
        user.first_name = fname
        user.last_name = lname
        user.number = number
        user.save()
        Customer.objects.get_or_create(phone=number, user=user, city=city,
                                       address=address, nickname=nickname,
                                       license_number=license_number, about=about,
                                       terms_condition=True)

        return redirect("customer:user_page")
    return render(request, "register/welcome.html")
