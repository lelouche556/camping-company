from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from genie.models import mainFrame, vehicleCleanliness, photos
from vehicle.models import Book


# Create your views here.

def create(request):
	print('i am here')
	return render(request,"genie/index.html")

# def showing(request):


def detail(request):
	book = Book.objects.all()
	return render(request,"genie/landing.html",{"book":book})



